import csv
from pathlib import Path

from relay_engine import RelaySettings, OvercurrentRelay, idmt_operate_time


RESULTS_DIR = Path("08_test_results")
RESULTS_DIR.mkdir(exist_ok=True)

CSV_PATH = RESULTS_DIR / "software_fat_results.csv"
REPORT_PATH = RESULTS_DIR / "software_fat_report.md"


def simulate_constant_current(current_a, duration_s, relay, dt_s=0.001, permissive=True):
    """
    Simulate constant current injection into the relay engine.
    Returns trip status, trip time and trip reason.
    """
    elapsed = 0.0

    while elapsed <= duration_s:
        state = relay.process_sample(
            current_a=current_a,
            dt_s=dt_s,
            permissive=permissive,
        )

        if state.trip:
            return {
                "tripped": True,
                "trip_time_s": elapsed,
                "trip_reason": state.trip_reason,
            }

        elapsed += dt_s

    return {
        "tripped": False,
        "trip_time_s": None,
        "trip_reason": "",
    }


def pass_fail_time(measured, expected, tolerance_s):
    if measured is None:
        return "FAIL"
    return "PASS" if abs(measured - expected) <= tolerance_s else "FAIL"


def main():
    settings = RelaySettings(
        pickup_a=300.0,
        tms=0.10,
        high_set_a=4000.0,
        high_set_delay_s=0.05,
    )

    tests = []

    # Below pickup test
    relay = OvercurrentRelay(settings)
    result = simulate_constant_current(
        current_a=250.0,
        duration_s=2.0,
        relay=relay,
        permissive=True,
    )

    tests.append({
        "test_id": "FAT-001",
        "description": "Below pickup should not trip",
        "injected_current_a": 250.0,
        "expected_result": "No trip",
        "expected_time_s": "",
        "measured_time_s": "" if result["trip_time_s"] is None else f"{result['trip_time_s']:.3f}",
        "trip_reason": result["trip_reason"],
        "verdict": "PASS" if not result["tripped"] else "FAIL",
    })

    # IDMT tests at 2x, 5x, 10x pickup
    for test_id, multiple in [
        ("FAT-002", 2),
        ("FAT-003", 5),
        ("FAT-004", 10),
    ]:
        injected_current = settings.pickup_a * multiple
        expected_time = idmt_operate_time(
            current_a=injected_current,
            pickup_a=settings.pickup_a,
            tms=settings.tms,
        )

        relay = OvercurrentRelay(settings)
        result = simulate_constant_current(
            current_a=injected_current,
            duration_s=expected_time + 0.5,
            relay=relay,
            permissive=True,
        )

        tolerance_s = max(0.02, expected_time * 0.05)
        verdict = pass_fail_time(result["trip_time_s"], expected_time, tolerance_s)

        tests.append({
            "test_id": test_id,
            "description": f"{multiple}x pickup IDMT trip time",
            "injected_current_a": injected_current,
            "expected_result": "Trip",
            "expected_time_s": f"{expected_time:.3f}",
            "measured_time_s": "" if result["trip_time_s"] is None else f"{result['trip_time_s']:.3f}",
            "trip_reason": result["trip_reason"],
            "verdict": verdict,
        })

    # Blocked permissive test
    relay = OvercurrentRelay(settings)
    result = simulate_constant_current(
        current_a=settings.pickup_a * 5,
        duration_s=2.0,
        relay=relay,
        permissive=False,
    )

    tests.append({
        "test_id": "FAT-005",
        "description": "Permissive open should block trip",
        "injected_current_a": settings.pickup_a * 5,
        "expected_result": "No trip, blocked",
        "expected_time_s": "",
        "measured_time_s": "" if result["trip_time_s"] is None else f"{result['trip_time_s']:.3f}",
        "trip_reason": result["trip_reason"],
        "verdict": "PASS" if not result["tripped"] else "FAIL",
    })

    # Below high-set short-duration test
    # 3588 A is the calculated feeder-end fault current from the fault study.
    # It is above pickup, so it can still trip by IDMT if held long enough.
    # This test is intentionally short: it proves it does not operate the 50 high-set element.
    relay = OvercurrentRelay(settings)
    result = simulate_constant_current(
        current_a=3588.0,
        duration_s=0.06,
        relay=relay,
        permissive=True,
    )

    tests.append({
        "test_id": "FAT-006",
        "description": "Feeder-end fault level should not cause instant high-set trip",
        "injected_current_a": 3588.0,
        "expected_result": "No high-set trip in short-duration test",
        "expected_time_s": "",
        "measured_time_s": "" if result["trip_time_s"] is None else f"{result['trip_time_s']:.3f}",
        "trip_reason": result["trip_reason"],
        "verdict": "PASS" if not result["tripped"] else "FAIL",
    })

    # High-set test
    # 4500 A is above the revised 4000 A high-set and below the 0-10 V full-scale range.
    relay = OvercurrentRelay(settings)
    result = simulate_constant_current(
        current_a=4500.0,
        duration_s=0.2,
        relay=relay,
        permissive=True,
    )

    tests.append({
        "test_id": "FAT-007",
        "description": "High-set overcurrent should trip after short delay",
        "injected_current_a": 4500.0,
        "expected_result": "Trip",
        "expected_time_s": f"{settings.high_set_delay_s:.3f}",
        "measured_time_s": "" if result["trip_time_s"] is None else f"{result['trip_time_s']:.3f}",
        "trip_reason": result["trip_reason"],
        "verdict": pass_fail_time(result["trip_time_s"], settings.high_set_delay_s, 0.01),
    })

    # Write CSV
    fieldnames = [
        "test_id",
        "description",
        "injected_current_a",
        "expected_result",
        "expected_time_s",
        "measured_time_s",
        "trip_reason",
        "verdict",
    ]

    with CSV_PATH.open("w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tests)

    # Write Markdown report
    with REPORT_PATH.open("w") as report:
        report.write("# Software FAT Report\n\n")
        report.write("## Purpose\n\n")
        report.write(
            "This report records software FAT-style tests for the simplified overcurrent relay engine. "
            "The tests inject defined current values and compare measured trip behaviour against expected IDMT or high-set operation.\n\n"
        )

        report.write("## Relay Settings Under Test\n\n")
        report.write("| Setting | Value |\n")
        report.write("|---|---:|\n")
        report.write(f"| Pickup | {settings.pickup_a:.0f} A |\n")
        report.write(f"| TMS | {settings.tms:.2f} |\n")
        report.write(f"| High-set | {settings.high_set_a:.0f} A |\n")
        report.write(f"| High-set delay | {settings.high_set_delay_s:.3f} s |\n\n")

        report.write("## High-Set Revision Note\n\n")
        report.write(
            "The high-set threshold is set to 4000 A. This is above the calculated feeder-end fault level "
            "of approximately 3588 A and below the calculated close-in/busbar-side finite-source fault level "
            "of approximately 4374 A. The software FAT tests below include a short-duration 3588 A case to prove "
            "that the high-set element does not operate below threshold, and a 4500 A case to prove high-set operation.\n\n"
        )

        report.write("## Test Results\n\n")
        report.write("| Test ID | Description | Injected current | Expected | Expected time | Measured time | Trip reason | Verdict |\n")
        report.write("|---|---|---:|---|---:|---:|---|---|\n")

        for test in tests:
            report.write(
                f"| {test['test_id']} | {test['description']} | "
                f"{test['injected_current_a']:.0f} A | {test['expected_result']} | "
                f"{test['expected_time_s']} | {test['measured_time_s']} | "
                f"{test['trip_reason']} | {test['verdict']} |\n"
            )

        report.write("\n## Limitations\n\n")
        report.write(
            "This is a software test harness for a demonstrator relay engine. "
            "It is not calibrated secondary injection and does not test a certified protection relay, CT circuit, "
            "breaker trip circuit or real relay firmware. The current values are simulated values used to test "
            "the simplified relay logic.\n"
        )

    print("Software FAT complete")
    print(f"Created: {CSV_PATH}")
    print(f"Created: {REPORT_PATH}")

    failed = [test for test in tests if test["verdict"] != "PASS"]
    if failed:
        print("Some tests failed:")
        for test in failed:
            print(f"- {test['test_id']}: {test['description']}")
        raise SystemExit(1)

    print("All tests passed")


if __name__ == "__main__":
    main()