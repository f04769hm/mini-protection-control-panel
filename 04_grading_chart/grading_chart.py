import math
import pandas as pd
import matplotlib.pyplot as plt

# Mini Protection & Control Panel
# Stage 2: IDMT relay grading chart

# IEC Standard Inverse curve constants.
# Formula: t = TMS * k / ((I / Is)^alpha - 1)
K_STANDARD_INVERSE = 0.14
ALPHA_STANDARD_INVERSE = 0.02

# Fault-study values from Stage 1
I_FAULT_BUSBAR = 4374      # A
I_FAULT_FEEDER_END = 3588  # A

# Simplified relay settings, primary current basis
RELAY_B_PICKUP = 300       # A, downstream feeder relay
RELAY_B_TMS = 0.10

RELAY_A_PICKUP = 600       # A, upstream backup relay
GRADING_MARGIN = 0.35      # s, simplified target grading margin

def idmt_time(current, pickup, tms, k=K_STANDARD_INVERSE, alpha=ALPHA_STANDARD_INVERSE):
    """Return IEC Standard Inverse IDMT operating time in seconds."""
    if current <= pickup:
        return math.inf
    multiple = current / pickup
    return tms * k / ((multiple ** alpha) - 1)

# Calculate Relay A TMS so it grades above Relay B at feeder-end fault
relay_b_time_at_feeder_end = idmt_time(I_FAULT_FEEDER_END, RELAY_B_PICKUP, RELAY_B_TMS)
relay_a_base_time_at_feeder_end = idmt_time(I_FAULT_FEEDER_END, RELAY_A_PICKUP, 1.0)
relay_a_tms_exact = (relay_b_time_at_feeder_end + GRADING_MARGIN) / relay_a_base_time_at_feeder_end

# Use rounded practical setting
RELAY_A_TMS = 0.17

print("Stage 2 grading calculation")
print("---------------------------")
print(f"Relay B pickup: {RELAY_B_PICKUP} A")
print(f"Relay B TMS: {RELAY_B_TMS}")
print(f"Relay A pickup: {RELAY_A_PICKUP} A")
print(f"Relay A exact TMS for {GRADING_MARGIN:.2f}s margin: {relay_a_tms_exact:.3f}")
print(f"Relay A selected TMS: {RELAY_A_TMS}")
print()
print(f"Relay B time at feeder-end fault ({I_FAULT_FEEDER_END} A): {relay_b_time_at_feeder_end:.3f} s")
print(f"Relay A time at feeder-end fault ({I_FAULT_FEEDER_END} A): {idmt_time(I_FAULT_FEEDER_END, RELAY_A_PICKUP, RELAY_A_TMS):.3f} s")
print(f"Actual margin: {idmt_time(I_FAULT_FEEDER_END, RELAY_A_PICKUP, RELAY_A_TMS) - relay_b_time_at_feeder_end:.3f} s")

# Generate curve data
currents = []
relay_b_times = []
relay_a_times = []

for current in range(250, 7001, 50):
    currents.append(current)
    relay_b_times.append(idmt_time(current, RELAY_B_PICKUP, RELAY_B_TMS))
    relay_a_times.append(idmt_time(current, RELAY_A_PICKUP, RELAY_A_TMS))

df = pd.DataFrame({
    "current_A": currents,
    "relay_B_time_s": relay_b_times,
    "relay_A_time_s": relay_a_times,
})

df.to_csv("04_grading_chart/curve_values.csv", index=False)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(currents, relay_b_times, label=f"Relay B downstream: pickup {RELAY_B_PICKUP} A, TMS {RELAY_B_TMS}")
plt.plot(currents, relay_a_times, label=f"Relay A upstream backup: pickup {RELAY_A_PICKUP} A, TMS {RELAY_A_TMS}")

plt.axvline(I_FAULT_FEEDER_END, linestyle="--", label=f"Feeder-end fault: {I_FAULT_FEEDER_END/1000:.1f} kA")
plt.axvline(I_FAULT_BUSBAR, linestyle=":", label=f"Busbar fault: {I_FAULT_BUSBAR/1000:.1f} kA")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Primary current (A)")
plt.ylabel("Operating time (s)")
plt.title("IDMT Overcurrent Grading Chart - IEC Standard Inverse")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("04_grading_chart/grading_chart.png", dpi=200)

print()
print("Created:")
print("04_grading_chart/grading_chart.png")
print("04_grading_chart/curve_values.csv")
