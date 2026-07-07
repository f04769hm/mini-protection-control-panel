\# Final Wiring Map



\## Purpose



This document defines the final wiring map for the Mini Protection \& Control Panel.



Assumption: all selected components have been confirmed suitable for 24 V DC extra-low-voltage use.



\## Controller



Controller: CODESYS Opta



\## Power Distribution



| Wire | From | To | Function |

|---|---|---|---|

| W001 | 24 V PSU + | F1 fuse input | Incoming 24 V positive |

| W002 | F1 fuse output | +24 V terminal rail | Fused 24 V distribution |

| W003 | 24 V PSU - | 0 V terminal rail | 0 V common |



\## Hardwired Circuits



\### Supply Healthy Lamp



| Wire | From | To |

|---|---|---|

| W004 | +24 V fused rail | Supply Healthy lamp + |

| W005 | Supply Healthy lamp - | 0 V rail |



\### Blocked Lamp



| Wire | From | To |

|---|---|---|

| W026 | +24 V fused rail | Block selector contact |

| W027 | Block selector contact | Blocked lamp + |

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



\### I3 Permissive Selector



| Wire | From | To |

|---|---|---|

| W010 | +24 V fused rail | Permissive selector contact |

| W011 | Permissive selector contact | Opta I3 |



\### I4 0–10 V Current Simulation



| Wire | From | To |

|---|---|---|

| W012 | 0–10 V simulator output + | Opta I4 analogue input |

| W013 | 0–10 V simulator 0 V | Opta analogue/common reference |



Important: confirm the signal is 0–10 V with a multimeter before connecting to Opta I4.



\## Opta Outputs



The Opta relay outputs are treated as dry contacts.



\### Q1 Trip Command



| Wire | From | To |

|---|---|---|

| W014 | +24 V fused rail | Opta Q1 common |

| W015 | Opta Q1 NO | Trip relay coil + |

| W016 | Trip relay coil - | 0 V rail |



\### Q2 Relay Healthy / Watchdog



| Wire | From | To |

|---|---|---|

| W017 | +24 V fused rail | Opta Q2 common |

| W018 | Opta Q2 NO | Relay Healthy lamp/relay + |

| W019 | Relay Healthy lamp/relay - | 0 V rail |



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



| Wire | From | To |

|---|---|---|

| W029 | +24 V fused rail | Trip relay load contact |

| W030 | Trip relay load contact | Load lamp/resistor + |

| W031 | Load lamp/resistor - | 0 V rail |



\## Intended Behaviour



Normal state:



\- Supply Healthy lamp on

\- Relay Healthy on

\- Load on

\- Pickup lamp off

\- Trip lamp off

\- Blocked lamp off if permissive is enabled



Pickup state:



\- Current input above 0.5 V

\- Pickup lamp on

\- IDMT operate progress increases



Trip state:



\- Trip command operates

\- Trip lamp on

\- Load switches off or changes state through trip relay contact

\- Trip remains latched until reset



Blocked state:



\- Permissive selector in block position

\- Blocked lamp on

\- Fault/current above pickup does not trip



Healthy failure state:



\- Opta power/program/output lost

\- Relay Healthy drops out

