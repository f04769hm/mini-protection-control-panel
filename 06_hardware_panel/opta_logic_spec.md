\# Opta Logic Specification



\## Purpose



This document defines the control logic for the Mini Protection \& Control Panel using the CODESYS Opta.



The physical panel demonstrates simplified protection and control behaviour:



\- simulated current input using a 0–10 V analogue signal

\- overcurrent pickup

\- IEC Standard Inverse IDMT trip logic

\- high-set overcurrent trip logic

\- software permissive/blocking status

\- hardwired permissive in the trip path

\- trip latch

\- manual reset

\- relay healthy/watchdog indication

\- fail-visible unhealthy/alarm indication

\- pickup and trip indication



This is not protection-class relay firmware. It is a low-voltage functional demonstrator.



\## I/O Allocation



\### Inputs



| Opta input | Tag | Type | Function |

|---|---|---|---|

| I1 | Fault\_Test\_PB | Digital input | Optional fault/test command |

| I2 | Reset\_PB | Digital input | Resets latched trip |

| I3 | Permissive | Digital input | Status input from selector PERMIT contact |

| I4 | Current\_Input\_V | Analogue input | 0–10 V simulated current signal |



\### Outputs



| Opta output | Tag | Type | Function |

|---|---|---|---|

| Q1 | Trip\_Command | Relay output | Energises trip relay when permissive is available |

| Q2 | Relay\_Healthy | Relay output | Energises healthy relay while logic is running |

| Q3 | Pickup\_Lamp | Relay output | Indicates current above pickup |

| Q4 | Trip\_Lamp | Relay output | Indicates trip latch operated |



\### Hardwired / Relay-Based Indication



| Device | Function |

|---|---|

| Supply Healthy lamp | Hardwired from fused 24 V DC supply |

| Blocked lamp | Hardwired from selector BLOCK contact |

| Relay Healthy lamp | Fed through healthy relay NO contact |

| Unhealthy / Alarm lamp | Fed through healthy relay NC contact |



\## Current Scaling



The first build uses a 0–10 V signal into Opta I4 to represent measured feeder current.



Version 1 does not measure real load current. It uses a controlled analogue signal as a secondary-injection-style current representation.



Formula:



Current\_A = Current\_Input\_V × 600



| Input voltage | Simulated primary current | Meaning |

|---:|---:|---|

| 0 V | 0 A | No current |

| 0.5 V | 300 A | 1× pickup |

| 1.0 V | 600 A | 2× pickup |

| 2.5 V | 1500 A | 5× pickup |

| 5.0 V | 3000 A | 10× pickup |

| 6.67 V | 4000 A | High-set threshold |

| 8.33 V | 5000 A | Above high-set test point |

| 10 V | 6000 A | Full-scale injection |



This means:



\- 300 A pickup = 0.5 V

\- 2× pickup = 1.0 V

\- 5× pickup = 2.5 V

\- 10× pickup = 5.0 V

\- 4000 A high-set = approximately 6.67 V



The 10 V full-scale signal represents 6000 A. This is enough for the finite-source demonstrator values but does not cover the 6.6 kA infinite-bus comparison case from the fault study.



The infinite-bus value is retained only as a sensitivity comparison, not as the main setting basis.



\## Relay Settings



| Setting | Value |

|---|---:|

| Pickup current | 300 A |

| TMS | 0.10 |

| Curve | IEC Standard Inverse |

| High-set current | 4000 A |

| High-set delay | 0.05 s |



\## High-Set Setting Basis



The high-set element was revised from 5000 A to 4000 A.



Reason:



\- calculated feeder-end fault current is approximately 3588 A

\- calculated close-in/busbar-side finite-source fault current is approximately 4374 A

\- the previous 5000 A high-set was above the calculated finite-source close-in fault level, so it would not operate for the modelled system



The revised 4000 A high-set sits above the feeder-end fault and below the close-in/busbar-side finite-source fault.



With the 0–10 V scaling:



4000 A / 600 = 6.67 V



So the hardware FAT can test high-set operation at approximately 7.0 V.



\## IEC Standard Inverse Equation



t = TMS × 0.14 / ((I / Is)^0.02 - 1)



Where:



\- t = operating time in seconds

\- TMS = time multiplier setting

\- I = measured/simulated current

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



The Relay\_Healthy output energises a healthy interface relay.



The healthy relay contacts provide visible indication:



\- healthy relay NO contact feeds the Relay Healthy lamp

\- healthy relay NC contact feeds the Unhealthy / Alarm lamp



If the Opta loses power or the program stops, the healthy relay drops out:



\- Relay Healthy lamp turns off

\- Unhealthy / Alarm lamp turns on



Limitation: this first version does not prove a true missing-pulse watchdog. A stronger future version would use a pulsed heartbeat and missing-pulse detector.



\### Permissive / Block



The permissive/block selector has two roles:



1\. It provides a software status input to Opta I3.

2\. It physically feeds or removes the +24 V trip-enable supply to Opta Q1 common.



If Permissive is true:



\- Opta I3 is true

\- Q1 common has a +24 V feed available

\- software trip logic is allowed to operate

\- the physical trip path is enabled



If Permissive is false:



\- Opta I3 is false

\- Q1 common has no +24 V feed

\- IDMT operate progress is reset

\- High-set timer is reset

\- Pickup may still be indicated if current is above pickup

\- Trip\_Command must not operate

\- even if Q1 were commanded, the trip relay coil cannot energise because the hardwired feed is removed



The Blocked lamp is hardwired from the selector BLOCK contact rather than controlled by the Opta.



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



\- start high-set timer

\- if timer >= High\_Set\_Delay, set trip latch



High-set trip reason:



50 high-set overcurrent



The high-set threshold is 4000 A, equivalent to approximately 6.67 V on the analogue input.



\### Trip Latch



Once trip latch is set:



\- Trip\_Command remains operated

\- Trip\_Lamp remains on

\- logic remains latched until Reset\_PB is pressed



\### Physical Trip Path



The final trip path is:



+24 V fused rail → selector PERMIT contact → Opta Q1 common → Opta Q1 NO → trip relay coil → 0 V



This means the selector provides a hardwired trip permissive.



In BLOCK, the trip relay coil cannot energise because Q1 common is not fed.



\## Simplified Logic Flow



1\. Read inputs

2\. Scale analogue current input to simulated current

3\. Check reset

4\. Set Relay\_Healthy output

5\. Check permissive/block status

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

| HT-005 | 7.0 V current input | High-set trip after short delay |

| HT-006 | Permissive open and fault applied | No trip, blocked indication shown |

| HT-007 | Reset pressed after trip | Trip latch clears |

| HT-008 | Controller power/program stopped | Relay Healthy drops out and Unhealthy / Alarm lamp turns on |

| HT-009 | Selector in BLOCK and Q1 commanded | Trip relay does not energise because Q1 common has no +24 V feed |



\## Notes for Implementation



Preferred implementation language: Structured Text.



Reason: the IDMT equation and operate-progress calculation are easier to implement and review in Structured Text than Ladder.



Ladder or Function Block Diagram can still be used later for pushbuttons, latch logic and simple indication, but the first working version should prioritise clarity and correctness.



\## Limitations



Version 1 uses a simulated 0–10 V current signal rather than real current measurement.



The load lamp/resistor is switched as a visual load representation, but its actual current is not measured by the Opta.



A later upgrade could use a 0–10 V current transducer or suitable analogue measurement chain to represent real measured load current.



The Relay Healthy output is not a true missing-pulse watchdog. It is a normally energised healthy output with fail-visible relay indication.

