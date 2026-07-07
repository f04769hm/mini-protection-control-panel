\# CODESYS Implementation Notes



\## Purpose



This note records how the Structured Text draft should be implemented on the CODESYS Opta.



The file `opta\_structured\_text.st` defines the relay logic, but physical I/O names must be mapped inside the actual CODESYS project once the Opta project is created.



\## Important Note



The Structured Text file uses readable variable names such as:



\- Fault\_Test\_PB

\- Reset\_PB

\- Permissive

\- Current\_Input\_V

\- Trip\_Command

\- Relay\_Healthy

\- Pickup\_Lamp

\- Trip\_Lamp



These are logical names. The actual Opta I/O mapping in CODESYS may use different device/channel names. The mapping must be confirmed in the CODESYS device tree.



\## Required I/O Mapping



| Logic variable | Physical point |

|---|---|

| Fault\_Test\_PB | Opta I1 |

| Reset\_PB | Opta I2 |

| Permissive | Opta I3 |

| Current\_Input\_V | Opta I4 analogue input |

| Trip\_Command | Opta Q1 |

| Relay\_Healthy | Opta Q2 |

| Pickup\_Lamp | Opta Q3 |

| Trip\_Lamp | Opta Q4 |



\## Current Scaling



The logic assumes that `Current\_Input\_V` is already represented in volts from 0 to 10 V.



If CODESYS gives a raw analogue value instead, the scaling must be adjusted.



Example:



If raw input is 0 to 10000 for 0 to 10 V:



Current\_Input\_V = Raw\_Input / 1000.0



Then:



Current\_A = Current\_Input\_V × 600



\## Cycle Time Warning



The draft uses:



Cycle\_Time\_s = 0.01



This assumes a 10 ms PLC cycle. The actual task cycle time should be set or confirmed in CODESYS.



If the PLC task cycle is different, update `Cycle\_Time\_s`.



\## Watchdog Limitation



The first version energises Relay\_Healthy while the program is running.



This proves the normally energised healthy-output concept, but it is not a true missing-pulse watchdog. A stronger future version would use a pulsed heartbeat and missing-pulse detector.



\## First CODESYS Test Procedure



1\. Create/open CODESYS Opta project.

2\. Add logical variables.

3\. Map inputs and outputs.

4\. Set or confirm PLC task cycle time.

5\. Confirm analogue input scaling.

6\. Test with no outputs wired first.

7\. Monitor variables online:

&#x20;  - Current\_Input\_V

&#x20;  - Current\_A

&#x20;  - Pickup

&#x20;  - Operate\_Progress

&#x20;  - Trip\_Latch

8\. Only after logic is confirmed, connect panel lamps/relays.

