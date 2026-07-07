# Fault Study

## Purpose

This section calculates simplified three-phase fault levels for a model 33/11 kV system. The purpose is to support overcurrent relay setting and grading calculations for a low-voltage protection and control demonstrator.

This is a simplified study using assumed values. It is not a replacement for a real DNO fault-level study.

## System Model

33 kV source → 33/11 kV transformer → 11 kV busbar → 11 kV feeder

Relay A = upstream backup relay  
Relay B = downstream feeder relay

Relay B should operate first for downstream feeder faults. Relay A should provide delayed backup.

## Assumptions

| Item | Assumed value | Notes |
|---|---:|---|
| Source fault level at 33 kV | 250 MVA | Assumed value; real value would come from the DNO/network operator |
| Transformer rating | 10 MVA | Assumed 33/11 kV transformer |
| Transformer impedance | 8% | Assumed transformer impedance |
| System base power | 100 MVA | Chosen calculation base |
| Base voltage at LV side | 11 kV | Nominal secondary voltage |
| Fault type | Three-phase bolted fault | Fault resistance ignored |
| Prefault voltage | 1.0 pu | Simplified assumption |

## Per-Unit Calculation

Base current at 11 kV:

I_base = S_base / (sqrt(3) × V_base)

I_base = 100,000,000 / (1.732 × 11,000)

I_base = 5,249 A

Source impedance:

Z_source = S_base / S_fault

Z_source = 100 / 250

Z_source = 0.4 pu

Transformer impedance on 100 MVA base:

Z_transformer = 0.08 × (100 / 10)

Z_transformer = 0.8 pu

Total impedance to 11 kV busbar:

Z_total = Z_source + Z_transformer

Z_total = 0.4 + 0.8

Z_total = 1.2 pu

Three-phase fault current at 11 kV busbar:

I_fault = I_base / Z_total

I_fault = 5,249 / 1.2

I_fault = 4,374 A

I_fault ≈ 4.4 kA

## Infinite-Bus Comparison

If the source impedance is ignored, the transformer-only impedance is 0.8 pu.

I_fault = 5,249 / 0.8

I_fault = 6,561 A

I_fault ≈ 6.6 kA

This shows that ignoring source impedance overestimates the available fault current. In this example, the infinite-bus approximation gives approximately 6.6 kA compared with approximately 4.4 kA when the assumed source fault level is included.

## Feeder-End Fault Current Extension

To estimate the downstream fault level at the end of the feeder, a representative 11 kV cable is added in series with the source and transformer impedance.

Representative cable used:

- Cable: 11 kV 3-core 185 mm² copper XLPE/SWA/PVC
- Standard: BS6622 / IEC 60502-2
- AC resistance at maximum temperature: 0.131 ohm/km
- Inductive reactance: 0.09 ohm/km
- Assumed feeder length: 2 km

The cable impedance per km is:

Z_cable_per_km = 0.131 + j0.09 ohm/km

For a 2 km feeder:

R_total = 0.131 × 2 = 0.262 ohm

X_total = 0.09 × 2 = 0.180 ohm

Magnitude of feeder impedance:

|Z_feeder| = sqrt(R_total² + X_total²)

|Z_feeder| = sqrt(0.262² + 0.180²)

|Z_feeder| = 0.318 ohm

Base impedance at 11 kV on 100 MVA base:

Z_base = V_base² / S_base

Z_base = 11,000² / 100,000,000

Z_base = 1.21 ohm

Feeder impedance in per-unit:

Z_feeder_pu = 0.318 / 1.21

Z_feeder_pu = 0.263 pu

Total impedance to feeder end:

Z_total_feeder_end = Z_source + Z_transformer + Z_feeder

Z_total_feeder_end = 0.4 + 0.8 + 0.263

Z_total_feeder_end = 1.463 pu

Three-phase fault current at feeder end:

I_fault_feeder_end = I_base / Z_total_feeder_end

I_fault_feeder_end = 5,249 / 1.463

I_fault_feeder_end = 3,588 A

I_fault_feeder_end ≈ 3.6 kA

## Results Summary

| Fault location | Total impedance | Fault current |
|---|---:|---:|
| 11 kV busbar, source + transformer | 1.2 pu | 4.4 kA |
| 11 kV feeder end, with 2 km 185 mm² cable | 1.463 pu | 3.6 kA |
| 11 kV busbar, transformer only / infinite bus | 0.8 pu | 6.6 kA |

## Cable Data Source

Cable resistance and reactance values are taken from a published technical specification for Nexans 11 kV 3-core 185 mm² BS6622 copper XLPE/SWA/PVC cable. The values used are 0.131 ohm/km AC resistance at maximum temperature and 0.09 ohm/km inductive reactance.

## Limitations

This simplified calculation assumes a single source, three-phase bolted fault, no motor contribution, no fault resistance, no transformer tap effects, and no feeder impedance. A real study would use confirmed network data, transformer data, cable impedance, protection CT ratios, and DNO-provided fault levels. For simplicity, impedances are treated using per-unit magnitude only; X/R ratio, DC offset and asymmetrical fault current are not considered.

## Next Extension

The next revision will add feeder-end fault current using a real cable datasheet. This will require selecting a representative 11 kV cable, obtaining R and X values in ohms/km, converting the feeder impedance to per-unit, and adding it in series with the source and transformer impedance.