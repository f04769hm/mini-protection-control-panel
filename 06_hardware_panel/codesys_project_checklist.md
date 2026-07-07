\# CODESYS Project Checklist



\## Purpose



This checklist defines the first implementation steps for the Mini Protection \& Control Panel on the CODESYS Opta.



The aim is to avoid improvising when the Opta is available.



\## Before Connecting Hardware



\- \[ ] Confirm the Opta model

\- \[ ] Confirm the Opta supply voltage

\- \[ ] Confirm CODESYS/Opta project template availability

\- \[ ] Confirm input voltage mode for I1-I4

\- \[ ] Confirm analogue input scaling for I4

\- \[ ] Confirm relay output behaviour for Q1-Q4

\- \[ ] Confirm task cycle time

\- \[ ] Confirm how variables are mapped to physical I/O

\- \[ ] Confirm no external load is wired during first software test



\## New CODESYS Project Setup



\- \[ ] Open CODESYS

\- \[ ] Create new project

\- \[ ] Select correct Opta device/profile

\- \[ ] Add or confirm PLC\_PRG

\- \[ ] Set task cycle time to 10 ms if possible

\- \[ ] Add logical variables from `opta\_structured\_text.st`

\- \[ ] Map physical inputs to logical variables

\- \[ ] Map physical outputs to logical variables

\- \[ ] Build/compile project

\- \[ ] Fix syntax/type errors

\- \[ ] Connect to Opta

\- \[ ] Download program

\- \[ ] Start PLC/runtime

\- \[ ] Monitor variables online



\## Logical Variable Mapping



| Logic variable | Physical point | Notes |

|---|---|---|

| Fault\_Test\_PB | Opta I1 | Digital input |

| Reset\_PB | Opta I2 | Digital input |

| Permissive | Opta I3 | Digital input |

| Current\_Input\_V | Opta I4 | 0-10 V analogue input |

| Trip\_Command | Opta Q1 | Relay output |

| Relay\_Healthy | Opta Q2 | Relay output |

| Pickup\_Lamp | Opta Q3 | Relay output |

| Trip\_Lamp | Opta Q4 | Relay output |



\## First Software-Only Checks



Before any external wiring is connected:



\- \[ ] Confirm program downloads successfully

\- \[ ] Confirm PLC runs without fault

\- \[ ] Confirm Relay\_Healthy variable is TRUE

\- \[ ] Force or simulate Current\_Input\_V below pickup

\- \[ ] Confirm Pickup is FALSE

\- \[ ] Force or simulate Current\_Input\_V above pickup

\- \[ ] Confirm Pickup is TRUE

\- \[ ] Force Permissive FALSE

\- \[ ] Confirm trip logic is blocked

\- \[ ] Force Reset\_PB TRUE

\- \[ ] Confirm Trip\_Latch resets



\## Output Safety



Do not connect output wiring until the logic has been tested online.



When output wiring is connected later:



\- Q1 must only switch the low-voltage load/trip circuit

\- Q2 must only switch the healthy relay/lamp circuit

\- Q3 must only switch the pickup lamp

\- Q4 must only switch the trip lamp



No mains voltage is to be switched.



\## Notes



The Structured Text draft may need minor adjustment once actual CODESYS input/output names and analogue scaling are confirmed.



Any changes made in CODESYS should be copied back into the GitHub repository so the repo stays authoritative.

