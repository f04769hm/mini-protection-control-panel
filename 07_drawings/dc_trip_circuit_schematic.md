\# DC Trip Circuit Schematic Draft



\## Purpose



This document defines the first DC wiring concept for the Mini Protection \& Control Panel.



The panel is a 24 V DC extra-low-voltage demonstrator. It does not switch mains voltage and is not connected to any live electrical installation.



\## Supply Distribution



```text

24 V DC PSU +

&#x20;     |

&#x20;     F1 Fuse

&#x20;     |

&#x20;     +24 V fused distribution rail

&#x20;     |

&#x20;     +---- Supply Healthy lamp ---- 0 V

&#x20;     |

&#x20;     +---- Opta supply +

&#x20;     |

&#x20;     +---- Input devices / lamps / load circuits



24 V DC PSU -

&#x20;     |

&#x20;     0 V distribution rail

&#x20;     |

&#x20;     +---- Opta supply -

&#x20;     |

&#x20;     +---- lamp returns

&#x20;     |

&#x20;     +---- load return



Input Circuits

I1 Fault/Test Pushbutton

+24 V fused ---- Fault/Test PB ---- Opta I1

0 V common ------------------------ Opta input common



Function:



Pressing the pushbutton sends a digital input to the Opta.

This can be used as a test/fault trigger.



I2 Reset Pushbutton

+24 V fused ---- Reset PB ---- Opta I2

0 V common ------------------ Opta input common



Function:



Pressing reset clears the trip latch.



I3 Permissive / Block Selector

+24 V fused ---- Permissive selector contact ---- Opta I3

0 V common -------------------------------------- Opta input common



Function:



Selector closed = permissive true.

Selector open = trip blocked.



Hardwired Blocked Lamp

+24 V fused ---- Block selector auxiliary/block contact ---- Blocked lamp ---- 0 V



Function:



The blocked lamp is hardwired from the selector switch.

It does not use an Opta output.



Analogue Current Simulation

I4 0–10 V Current Input

0–10 V simulator output + ---- Opta I4 analogue input

0–10 V simulator 0 V --------- Opta analogue/common reference



Scaling:



Current\_A = Input\_V × 600



Examples:



Input voltage	Simulated current

&#x09;0.5 V		300 A

&#x09;1.0 V		600 A

&#x09;2.5 V		1500 A

&#x09;5.0 V		3000 A

&#x09;8.33 V		5000 A



Safety rule:



The analogue signal must be checked with a multimeter before connection to the Opta. It must not exceed 10 V.



Output Circuits



The Opta relay outputs are treated as dry contacts.



Q1 Trip / Load Opening



First build option:



+24 V fused ---- Opta Q1 contact ---- Trip relay coil ---- 0 V



Trip relay contact then switches the load:



+24 V fused ---- Trip relay contact ---- Load lamp/resistor ---- 0 V



Function:



Opta Q1 energises the trip relay.

The trip relay contact opens or switches the load circuit, depending on final contact arrangement.

Q2 Relay Healthy / Watchdog

+24 V fused ---- Opta Q2 contact ---- Healthy relay/lamp ---- 0 V



Function:



Relay Healthy is normally energised while the Opta logic is running.

If the Opta loses power/program stops/output drops, healthy indication drops out.



Limitation:



This first version is a normally energised healthy output, not a true missing-pulse watchdog.



Q3 Pickup Lamp

+24 V fused ---- Opta Q3 contact ---- Pickup lamp ---- 0 V



Function:

Lamp on when measured/simulated current is above pickup.



Q4 Trip Lamp

+24 V fused ---- Opta Q4 contact ---- Trip lamp ---- 0 V



Function:

Lamp on when trip latch is operated.



Notes



Final contact numbering depends on the actual relay/socket parts used.



The final wiring must be checked against actual device datasheets and terminal markings before energising.

