\# Final Wiring Map



\## Purpose



This document defines the final wiring map for the Mini Protection \& Control Panel.



Assumption: all selected components have been confirmed suitable for 24 V DC extra-low-voltage use.



This revision fixes the trip permissive so that blocking is hardwired, not only software-based.



\## Controller



Controller: CODESYS Opta



\## Key Design Decisions



\### 1. Hardwired permissive



The permissive/block selector is wired into the physical trip path.



This means that when the selector is in BLOCK, the trip relay coil cannot energise even if the Opta software commands a trip.



This preserves the hardwired interlocking/permissive concept.



\### 2. Selector switch requirement



The selector switch must provide either:



\- one changeover contact, or

\- enough contact blocks to provide one PERMIT contact and one BLOCK indication contact.



The PERMIT contact feeds the trip path and Opta I3.



The BLOCK contact feeds the hardwired Blocked lamp.



Do not use a single-contact selector unless the blocked indication and trip permissive wiring can still be achieved.



\### 3. Current input is simulated



Version 1 uses a controlled 0–10 V signal to represent measured current.



It does not measure real feeder/load current.



Scaling:



Current\_A = Input\_V × 600



| Input voltage | Simulated current | Meaning |

|---:|---:|---|

| 0.5 V | 300 A | 1× pickup |

| 1.0 V | 600 A | 2× pickup |

| 2.5 V | 1500 A | 5× pickup |

| 5.0 V | 3000 A | 10× pickup |

| 8.33 V | 5000 A | High-set threshold |



The 0–10 V source must be verified with a multimeter before connection to Opta I4.



\### 4. Trip arrangement



Version 1 uses energise-to-trip.



The Opta energises a trip relay coil. The feeder load is wired through the trip relay NC contact. When the relay energises, the NC contact opens and the load switches off.



Real schemes may use different trip arrangements, including de-energise-to-trip, trip circuit supervision and more robust fail-safe designs. This demonstrator uses energise-to-trip for clarity and safe low-voltage demonstration.



\### 5. Healthy / unhealthy indication



The Relay Healthy output energises a healthy interface relay.



\- Healthy relay NO contact feeds the Relay Healthy lamp.

\- Healthy relay NC contact feeds the Unhealthy / Alarm lamp.



So if the healthy relay drops out, the alarm becomes visible.



Limitation: this is not a true missing-pulse watchdog. A software hang could theoretically leave the output energised. A future improvement would use a pulsed heartbeat and missing-pulse detector.



\## Power Distribution



| Wire | From | To | Function |

|---|---|---|---|

| W001 | 24 V PSU + | F1 fuse input | Incoming 24 V positive |

| W002 | F1 fuse output | +24 V terminal rail | Fused 24 V distribution |

| W003 | 24 V PSU - | 0 V terminal rail | 0 V common |

| W032 | +24 V fused rail | Opta supply + | Opta power positive |

| W033 | 0 V rail | Opta supply - | Opta power return |



\## Hardwired Supply Indication



\### Supply Healthy Lamp



| Wire | From | To |

|---|---|---|

| W004 | +24 V fused rail | Supply Healthy lamp + |

| W005 | Supply Healthy lamp - | 0 V rail |



\## Hardwired Blocked Indication



\### Blocked Lamp



The blocked lamp is wired from the selector’s BLOCK contact, not from an Opta output.



| Wire | From | To |

|---|---|---|

| W026 | +24 V fused rail | Selector BLOCK contact common |

| W027 | Selector BLOCK contact output | Blocked lamp + |

| W028 | Blocked lamp - | 0 V rail |



\## Opta Inputs



\### I1 Fault/Test Pushbutton



| Wire | From | To |

|---|---|---|

| W006 | +24 V fused rail | Fault/Test pushbutton |

| W007 | Fault/Test pushbutton | Opta I1 |



\### I2 Reset Pushbutton



| Wire | From | To |

|---|---|---|

| W008 | +24 V fused rail | Reset pushbutton |

| W009 | Reset pushbutton | Opta I2 |



\### I3 Permissive Status Input



Opta I3 is taken from the same PERMIT contact feed that enables the trip path.



| Wire | From | To |

|---|---|---|

| W010 | +24 V fused rail | Selector PERMIT contact common |

| W011 | Selector PERMIT contact output | Opta I3 |



Function:



\- Selector in PERMIT = Opta I3 true and trip path feed available.

\- Selector in BLOCK = Opta I3 false and trip path physically blocked.



\### I4 0–10 V Current Simulation



| Wire | From | To |

|---|---|---|

| W012 | 0–10 V signal source output + | Opta I4 analogue input |

| W013 | 0–10 V signal source 0 V | Opta analogue/common reference |



Important:



The 0–10 V source must be checked with a multimeter before connecting to Opta I4.



It must not exceed 10 V.



\## Opta Outputs



The Opta relay outputs are treated as dry contacts.



\### Q1 Trip Command With Hardwired Permissive



Q1 common is fed through the selector PERMIT contact.



This means BLOCK physically prevents the trip relay coil energising.



| Wire | From | To |

|---|---|---|

| W010 | +24 V fused rail | Selector PERMIT contact common |

| W034 | Selector PERMIT contact output | Opta Q1 common |

| W015 | Opta Q1 NO | Trip relay coil + |

| W016 | Trip relay coil - | 0 V rail |



Note:



W011 and W034 are electrically the same permissive-fed node if taken from the same selector output. W011 goes to Opta I3 as status. W034 feeds Opta Q1 common for the trip path.



\### Q2 Relay Healthy / Watchdog Relay



| Wire | From | To |

|---|---|---|

| W017 | +24 V fused rail | Opta Q2 common |

| W018 | Opta Q2 NO | Healthy relay coil + |

| W019 | Healthy relay coil - | 0 V rail |



Healthy relay indication contacts:



| Wire | From | To |

|---|---|---|

| W035 | +24 V fused rail | Healthy relay NO common |

| W036 | Healthy relay NO output | Relay Healthy lamp + |

| W037 | Relay Healthy lamp - | 0 V rail |

| W038 | +24 V fused rail | Healthy relay NC common |

| W039 | Healthy relay NC output | Unhealthy / Alarm lamp + |

| W040 | Unhealthy / Alarm lamp - | 0 V rail |



\### Q3 Pickup Lamp



| Wire | From | To |

|---|---|---|

| W020 | +24 V fused rail | Opta Q3 common |

| W021 | Opta Q3 NO | Pickup lamp + |

| W022 | Pickup lamp - | 0 V rail |



\### Q4 Trip Lamp



| Wire | From | To |

|---|---|---|

| W023 | +24 V fused rail | Opta Q4 common |

| W024 | Opta Q4 NO | Trip lamp + |

| W025 | Trip lamp - | 0 V rail |



\## Load Circuit



The load is wired through the trip relay NC contact.



Normal state:



\- Trip relay de-energised

\- NC contact closed

\- Load on



Trip state:



\- Trip relay energised

\- NC contact opens

\- Load switches off



| Wire | From | To |

|---|---|---|

| W029 | +24 V fused rail | Trip relay NC contact common |

| W030 | Trip relay NC contact output | Load lamp/resistor + |

| W031 | Load lamp/resistor - | 0 V rail |



\## Intended Behaviour



\### Normal state



\- Supply Healthy lamp on

\- Relay Healthy lamp on

\- Unhealthy / Alarm lamp off

\- Load on

\- Pickup lamp off

\- Trip lamp off

\- Blocked lamp off if permissive is enabled



\### Pickup state



\- Current input above 0.5 V

\- Pickup lamp on

\- IDMT operate progress increases



\### Trip state



\- Opta Q1 energises trip relay

\- Trip lamp on

\- Trip relay NC contact opens

\- Load switches off

\- Trip remains latched until reset



\### Blocked state



\- Selector in BLOCK position

\- Blocked lamp on

\- Opta I3 false

\- Q1 trip path physically has no +24 V feed

\- Fault/current above pickup does not energise trip relay



\### Healthy failure state



\- Opta power/program/output lost

\- Healthy relay drops out

\- Relay Healthy lamp turns off

\- Unhealthy / Alarm lamp turns on through healthy relay NC contact



\## Ratings To Confirm Before Wiring



| Item | Rating to confirm |

|---|---|

| 24 V PSU | Output current capacity |

| F1 fuse | Fuse current rating |

| Opta | Exact model and supply/input details |

| Trip relay coil | 24 V DC coil current |

| Trip relay contact | Suitable for 24 V load current |

| Healthy relay coil | 24 V DC coil current |

| Lamps | 24 V DC and lamp current |

| Load lamp/resistor | Voltage, current and power dissipation |

| 0–10 V source | Output limited to 10 V maximum |

| Selector switch | PERMIT and BLOCK/changeover contacts |

