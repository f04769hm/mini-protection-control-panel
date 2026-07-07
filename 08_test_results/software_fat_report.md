# Software FAT Report

## Purpose

This report records software FAT-style tests for the simplified overcurrent relay engine. The tests inject defined current values and compare measured trip behaviour against expected IDMT or high-set operation.

## Relay Settings Under Test

| Setting | Value |
|---|---:|
| Pickup | 300 A |
| TMS | 0.10 |
| High-set | 5000 A |
| High-set delay | 0.050 s |

## Test Results

| Test ID | Description | Injected current | Expected | Expected time | Measured time | Trip reason | Verdict |
|---|---|---:|---|---:|---:|---|---|
| FAT-001 | Below pickup should not trip | 250 A | No trip |  |  |  | PASS |
| FAT-002 | 2x pickup IDMT trip time | 600 A | Trip | 1.003 | 1.002 | 51 IDMT overcurrent | PASS |
| FAT-003 | 5x pickup IDMT trip time | 1500 A | Trip | 0.428 | 0.427 | 51 IDMT overcurrent | PASS |
| FAT-004 | 10x pickup IDMT trip time | 3000 A | Trip | 0.297 | 0.297 | 51 IDMT overcurrent | PASS |
| FAT-005 | Permissive open should block trip | 1500 A | No trip, blocked |  |  |  | PASS |
| FAT-006 | High-set overcurrent should trip after short delay | 6000 A | Trip | 0.050 | 0.049 | 50 high-set overcurrent | PASS |

## Limitations

This is a software test harness for a demonstrator relay engine. It is not calibrated secondary injection and does not test a certified protection relay, CT circuit, breaker trip circuit or real relay firmware.
