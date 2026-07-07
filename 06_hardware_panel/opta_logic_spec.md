\# Opta Logic Specification



\## Purpose



This document defines the control logic for the Mini Protection \& Control Panel using the CODESYS Opta.



The physical panel demonstrates simplified protection and control behaviour:



\- current measurement / simulated current input

\- overcurrent pickup

\- IEC Standard Inverse IDMT trip logic

\- high-set overcurrent trip logic

\- permissive/blocking

\- trip latch

\- manual reset

\- relay healthy/watchdog indication

\- pickup and trip indication



This is not protection-class relay firmware. It is a low-voltage functional demonstrator.



\## I/O Allocation



\### Inputs



| Opta input | Tag | Type | Function |

|---|---|---|---|

| I1 | Fault\_Test\_PB | Digital input | Optional fault/test command |

| I2 | Reset\_PB | Digital input | Resets latched trip |

| I3 | Permissive | Digital input | Allows trip when closed/true |

| I4 | Current\_Input\_V | Analogue input | 0–10 V simulated current signal |



\### Outputs



| Opta output | Tag | Type | Function |

|---|---|---|---|

| Q1 | Trip\_Command | Relay output | Opens/switches feeder load circuit |

| Q2 | Relay\_Healthy | Relay output | Normally energised healthy/watchdog output |

| Q3 | Pickup\_Lamp | Relay output | Indicates current above pickup |

| Q4 | Trip\_Lamp | Relay output | Indicates trip latch operated |



\### Hardwired Indication



| Device | Function |

|---|---|

| Supply Healthy lamp | Hardwired from fused 24 V DC supply |

| Blocked lamp | Hardwired from permissive/block selector switch auxiliary contact |



\## Current Scaling



The first build uses a 0–10 V signal into Opta I4 to represent measured feeder current.



Scaling:



| Input voltage | Simulated primary current |

|---:|---:|

| 0 V | 0 A |

| 0.5 V | 300 A |

| 1.0 V | 600 A |

| 2.5 V | 1500 A |

| 5.0 V | 3000 A |

| 8.33 V | 5000 A |

| 10 V | 6000 A |



Formula:



Current\_A = Current\_Input\_V × 600



This means:



\- 300 A pickup = 0.5 V

\- 2× pickup = 1.0 V

\- 5× pickup = 2.5 V

\- 10× pickup = 5.0 V

\- 5000 A high-set = approximately 8.33 V



\## Relay Settings



| Setting | Value |

|---|---:|

| Pickup current | 300 A |

| TMS | 0.10 |

| Curve | IEC Standard Inverse |

| High-set current | 5000 A |

| High-set delay | 0.05 s |



IEC Standard Inverse equation:



t = TMS × 0.14 / ((I / Is)^0.02 - 1)



Where:



\- t = operating time in seconds

\- TMS = time multiplier setting

\- I = measured current

\- Is = pickup current



\## Logic Behaviour



\### Reset



If Reset\_PB is pressed:



\- Trip latch is reset

\- IDMT operate progress is reset

\- High-set timer is reset

\- Trip\_Command is de-energised

\- Trip\_Lamp is turned off



\### Relay Healthy / Watchdog



Relay\_Healthy is normally energised while the controller logic is running.



If the Opta loses power or the program stops, the healthy output drops out.



Limitation: this first version does not prove a true missing-pulse watchdog. A stronger future version would use a pulsed heartbeat and missing-pulse detector.



\### Permissive / Block



If Permissive is false:



\- Trip operation is blocked

\- IDMT operate progress is reset

\- High-set timer is reset

\- Pickup may still be indicated if current is above pickup

\- Trip\_Command must not operate



The Blocked lamp is hardwired from the selector switch rather than controlled by the Opta.



\### Pickup



If Current\_A > Pickup\_Current:



\- Pickup\_Lamp is energised



If Current\_A <= Pickup\_Current:



\- Pickup\_Lamp is de-energised

\- IDMT operate progress is reset



\### IDMT Trip



If Current\_A > Pickup\_Current and Permissive is true:



1\. Calculate IDMT operate time.

2\. Add progress each PLC cycle:



Operate\_Progress = Operate\_Progress + Cycle\_Time / Operate\_Time



3\. If Operate\_Progress >= 1.0:



\- Trip latch is set

\- Trip reason = 51 IDMT overcurrent

\- Trip\_Command operates

\- Trip\_Lamp energises



\### High-Set Trip



If Current\_A >= High\_Set\_Current and Permissive is true:



\- Start high-set timer

\- If timer >= High\_Set\_Delay, set trip latch



High-set trip reason:



50 high-set overcurrent



\### Trip Latch



Once trip latch is set:



\- Trip\_Command remains operated

\- Trip\_Lamp remains on

\- Logic remains latched until Reset\_PB is pressed



\## Simplified Logic Flow



1\. Read inputs

2\. Scale analogue current input to simulated current

3\. Check reset

4\. Set Relay\_Healthy output

5\. Check permissive/block

6\. Check pickup

7\. Run high-set timer

8\. Run IDMT operate-progress calculation

9\. Set/reset outputs

10\. Repeat every PLC cycle



\## Test Points



| Test ID | Test | Expected result |

|---|---|---|

| HT-001 | 0 V current input | No pickup, no trip |

| HT-002 | 1.0 V current input | 2× pickup IDMT trip after calculated delay |

| HT-003 | 2.5 V current input | 5× pickup IDMT trip after calculated delay |

| HT-004 | 5.0 V current input | 10× pickup IDMT trip after calculated delay |

| HT-005 | 8.5 V current input | High-set trip after short delay |

| HT-006 | Permissive open and fault applied | No trip, blocked indication shown |

| HT-007 | Reset pressed after trip | Trip latch clears |

| HT-008 | Controller power/program stopped | Relay Healthy drops out |



\## Notes for Implementation



Preferred implementation language: Structured Text.



Reason: the IDMT equation and operate-progress calculation are easier to implement and review in Structured Text than Ladder.



Ladder or Function Block Diagram can still be used later for pushbuttons, latch logic and simple indication, but the first working version should prioritise clarity and correctness.

