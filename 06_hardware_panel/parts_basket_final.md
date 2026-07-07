\# Parts Basket Final Draft



\## Controller



| Item | Status | Notes |

|---|---|---|

| CODESYS Opta | Borrow/use for a few months | Main controller for the physical panel |

| Raspberry Pi 4 | Available | Reserved for separate future IEC 61850/GOOSE lab, not this build |



\## Likely Available Through Work / Proper Permission



The following items may be available through proper work channels or scrap/offcut stock:



| Item | Status | Notes |

|---|---|---|

| Interface relays | Likely available | Use for trip/healthy circuits if suitable coil/contact ratings |

| DIN rail | Likely available | Offcut rail is ideal |

| Terminal blocks | Likely available | Use for +24 V, 0 V, inputs, outputs and load wiring |

| Panel wire | Likely available | Use sensible colours where possible |

| Ferrules | Likely available | Use on all stranded wire terminations |



These items must only be used with permission. Nothing should be taken without approval.



\## Must-Have Panel Parts



| Item | Quantity | Notes |

|---|---:|---|

| 24 V DC DIN-rail power supply | 1 | Small unit is fine; keep everything extra-low-voltage |

| DIN rail / backboard / small enclosure | 1 | Main presentation upgrade; should look like a mini panel |

| Terminal blocks | 10–20 | For +24 V, 0 V, inputs, outputs and load wiring |

| End stops / terminal markers | As needed | Makes the wiring look professional |

| Ferrules | Assorted | Use on stranded wire |

| Ferrule crimper | 1 | Borrow if possible |

| Wire labels / marker sleeves | As needed | Match wiring to I/O list |

| 24 V indicator lamps | 5 | Supply Healthy, Relay Healthy, Pickup, Trip, Blocked |

| Momentary pushbutton | 2 | Fault/Test and Reset |

| Maintained selector switch | 1 | Permissive / Block |

| 24 V interface relay | 1 | Relay Healthy / watchdog if not using Opta output directly to lamp |

| 24 V load lamp or low-power load | 1 | Represents feeder load |

| Fuse holder + small DC fuse | 1 | Protect 24 V supply/load circuit |

| Panel wire | As needed | Prefer sensible colours if available |



\## Current / Fault Simulation Options



\### Option A — safest first build: 0–10 V potentiometer as current simulator



Use a 0–10 V signal into Opta I4 to represent measured current.



Pros:

\- easiest

\- cheap

\- no sensor compatibility drama

\- directly proves analogue input, pickup, IDMT and trip logic



Cons:

\- not physically measuring load current yet



\### Option B — later upgrade: real current sensor



Use a current sensor only if its output is safely compatible with the Opta analogue input.



Required:

\- output must stay within 0–10 V

\- output must share a safe reference with the controller input

\- load current must stay inside the sensor rating

\- sensor wiring must be documented



\## Output Allocation



| Opta output | Function |

|---|---|

| Q1 | Trip / open load |

| Q2 | Relay Healthy / watchdog |

| Q3 | Pickup lamp |

| Q4 | Trip lamp |



Blocked lamp is hardwired from the permissive/block selector switch, not driven by Opta output.



\## Input Allocation



| Opta input | Function |

|---|---|

| I1 | Fault/Test pushbutton |

| I2 | Reset pushbutton |

| I3 | Permissive/Block switch |

| I4 | 0–10 V current simulation / current signal |

| I5–I8 | Spare |



\## Do Not Buy



\- used protection relay

\- relay test set

\- Node-RED/MQTT/SCADA hardware

\- pfSense/networking hardware

\- IEC 61850/GOOSE equipment

\- random relay boards unless trigger voltage and coil voltage are confirmed



\## Compatibility Rules



1\. Keep panel/control voltage at 24 V DC.

2\. Treat Opta analogue input as 0–10 V maximum.

3\. Do not feed uncontrolled 24 V into an analogue input.

4\. Use Opta relay outputs as dry contacts, not powered outputs.

5\. Fuse the load branch.

6\. Keep everything extra-low-voltage.

7\. No mains switching.

