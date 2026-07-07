\# Procurement Plan



\## Purpose



This document records what can likely be sourced through proper work channels and what still needs buying/finding for the Mini Protection \& Control Panel.



The aim is to keep the build cheap while spending only on items that directly improve the physical demonstrator.



\## Likely Available Through Work / Proper Permission



| Item | Status | Notes |

|---|---|---|

| CODESYS Opta | Likely available temporarily | Main controller for the physical panel |

| 24 V DC power supply | Likely available | Panel/control supply |

| DIN rail | Likely available | Use offcut if permitted |

| Terminal blocks | Likely available | For clean wiring and terminal schedule |

| Interface relays | Likely available | Use for trip/healthy circuits if ratings match |

| Panel wire | Likely available | Use sensible colours where practical |

| Ferrules | Likely available | Use on stranded wires |

| Ferrule crimper | Likely available | Borrow/use with permission |

| Wire labels / label maker | Likely available | Match wiring to I/O and terminal schedule |

| 24 V lamps | Likely available | Supply Healthy, Relay Healthy, Pickup, Trip, Blocked |

| Load lamp/resistor | Possibly available in lab | Confirm rating before use |



All items must be obtained through proper permission. Nothing should be taken without approval.



\## To Buy or Find



| Item | Priority | Notes |

|---|---|---|

| Fault/Test pushbutton | Required | Momentary type |

| Reset pushbutton | Required | Momentary type |

| Permissive selector switch | Required | Maintained 2-position selector |

| Fuse holder + fuse | Required | For 24 V panel/load protection |

| 0–10 V signal generator/current simulator | Required | Must output safe 0–10 V signal to Opta analogue input |

| Load lamp/resistor | Required if not available | Must be safely rated for the 24 V supply |



\## Explicitly Out of Scope for Version 1



The following may be available but are not part of the first build:



| Item | Reason |

|---|---|

| Energy meter | Distracts from protection/control objective |

| Power analyser | Useful later but not required for IDMT demo |

| SPD | Not required for extra-low-voltage demonstrator |

| Fan/heater/thermostat | Pulls the project toward HVAC/control rather than P\&C |

| Opta expansion modules | Base Opta I/O is enough for v1 |

| SCADA/HMI hardware | Not part of this build |

| IEC 61850/GOOSE hardware | Separate future project only |



\## 0–10 V Current Simulator Rule



The Opta analogue input must be treated as a 0–10 V input.



Do not wire a potentiometer directly across 24 V and feed the wiper into the analogue input.



Acceptable options:



1\. Proper 0–10 V signal generator module.

2\. 10 V reference plus potentiometer.

3\. Verified analogue output module configured for 0–10 V.



The chosen method must be tested with a multimeter before connecting to the Opta input.



\## Minimum Spend Target



Because most panel parts may be available through work, personal spend should be limited to the missing control devices and the 0–10 V simulator.



Spend money only where it directly enables:



\- safe 24 V wiring

\- clean panel presentation

\- input simulation

\- repeatable testing

