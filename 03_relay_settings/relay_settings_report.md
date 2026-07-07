\# Relay Settings Report



\## Purpose



This report defines simplified overcurrent settings for a model 33/11 kV system with a downstream feeder relay and an upstream backup relay.



The aim is to demonstrate the protection-setting workflow: selecting pickup values, applying an IEC Standard Inverse IDMT curve, grading the upstream relay above the downstream relay, and documenting assumptions and limitations.



\## System Summary



Relay A = upstream backup relay  

Relay B = downstream feeder relay



Relay B should operate first for feeder faults. Relay A should provide delayed backup.



Fault-current values from Stage 1:



| Fault location | Fault current |

|---|---:|

| 11 kV busbar fault | 4.4 kA |

| 11 kV feeder-end fault | 3.6 kA |



\## Curve Used



The curve used is IEC Standard Inverse.



Formula:



t = TMS × 0.14 / ((I / Is)^0.02 - 1)



Where:



\- t = relay operating time in seconds

\- TMS = time multiplier setting

\- I = fault current

\- Is = relay pickup current



\## Selected Settings



| Relay | Role | Pickup | TMS | Curve |

|---|---|---:|---:|---|

| Relay B | Downstream feeder relay | 300 A | 0.10 | IEC Standard Inverse |

| Relay A | Upstream backup relay | 600 A | 0.17 | IEC Standard Inverse |



\## Grading Check at Feeder-End Fault



At the feeder-end fault current of 3.588 kA:



| Relay | Operating time |

|---|---:|

| Relay B | approximately 0.275 s |

| Relay A | approximately 0.654 s |



Grading margin:



Relay A time - Relay B time = approximately 0.379 s



This gives the downstream Relay B time to operate first, while Relay A remains as delayed backup.



\## Explanation of Pickup Choices



Relay B is set with a lower pickup because it protects the downstream feeder.



Relay A is set with a higher pickup and longer time multiplier because it acts as upstream backup. It should not operate before Relay B for downstream feeder faults.



The pickup values are simplified demonstration settings on a primary-current basis. In a real protection study, pickup settings would be based on load current, CT ratios, equipment ratings, minimum fault level, protection sensitivity, discrimination requirements and network operator standards.



\## Limitations



This is a simplified settings study for a low-voltage demonstrator.



It does not include real CT ratios, CT saturation checks, relay manufacturer setting granularity, breaker operating time, relay overshoot, full grading-margin breakdown, earth-fault protection, motor contribution, transformer inrush, fuse coordination or real network fault-level data.



The hardware demonstrator is not a protection-class relay or CT measurement chain.

