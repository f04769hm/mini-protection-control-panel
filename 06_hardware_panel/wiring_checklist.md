\# Wiring Checklist



\## Purpose



This checklist defines the safe wiring order for the Mini Protection \& Control Panel.



The panel is a 24 V DC extra-low-voltage demonstrator. It must not switch mains voltage and must not be connected to any live electrical installation.



\## Build Order



\### 1. Mechanical mounting



\- \[ ] Mount DIN rail or backboard

\- \[ ] Mount Opta

\- \[ ] Mount terminal blocks

\- \[ ] Mount interface relays

\- \[ ] Mount lamps

\- \[ ] Mount pushbuttons

\- \[ ] Mount selector switch

\- \[ ] Mount fuse holder

\- \[ ] Mount load lamp/resistor



\### 2. Power supply checks



\- \[ ] Confirm 24 V DC supply rating

\- \[ ] Confirm supply polarity

\- \[ ] Add fuse on +24 V feed

\- \[ ] Wire +24 V and 0 V to terminal blocks

\- \[ ] Check +24 V to 0 V with multimeter

\- \[ ] Confirm no short circuit between +24 V and 0 V



\### 3. Hardwired indications



\- \[ ] Wire Supply Healthy lamp from fused 24 V DC

\- \[ ] Wire Blocked lamp from permissive/block selector auxiliary contact

\- \[ ] Test Supply Healthy lamp

\- \[ ] Test Blocked lamp changes with selector switch



\### 4. Opta input wiring



\- \[ ] Wire Fault/Test pushbutton to Opta I1

\- \[ ] Wire Reset pushbutton to Opta I2

\- \[ ] Wire Permissive/Block selector to Opta I3

\- \[ ] Wire 0–10 V current simulation signal to Opta I4

\- \[ ] Confirm input common/reference wiring

\- \[ ] Confirm no 24 V is accidentally connected to analogue input if using 0–10 V mode



\### 5. Opta output wiring



\- \[ ] Wire Q1 to Trip Command circuit

\- \[ ] Wire Q2 to Relay Healthy / watchdog circuit

\- \[ ] Wire Q3 to Pickup lamp

\- \[ ] Wire Q4 to Trip lamp

\- \[ ] Confirm Opta relay outputs are used as contacts, not assumed powered outputs

\- \[ ] Confirm contact ratings are suitable for 24 V DC demonstrator load



\### 6. Load/trip circuit



\- \[ ] Wire 24 V supply through fuse

\- \[ ] Wire trip relay/contact in series with load

\- \[ ] Wire load return to 0 V

\- \[ ] Confirm load current is within supply, fuse and relay-contact ratings

\- \[ ] Confirm trip contact opens/switches the load as intended



\### 7. Pre-power checks



\- \[ ] Tug-test wires gently

\- \[ ] Check ferrules/crimps

\- \[ ] Check terminal tightness

\- \[ ] Check wire labels match I/O list

\- \[ ] Check no loose strands

\- \[ ] Check no exposed conductor where not intended

\- \[ ] Check polarity before powering



\### 8. First power-up



\- \[ ] Power 24 V supply only

\- \[ ] Confirm Supply Healthy lamp

\- \[ ] Confirm Opta powers up

\- \[ ] Confirm no abnormal heating/smell/noise

\- \[ ] Confirm no fuse operation

\- \[ ] Confirm outputs remain safe before loading program



\### 9. Logic test before load



\- \[ ] Monitor variables in CODESYS

\- \[ ] Confirm Fault/Test input changes

\- \[ ] Confirm Reset input changes

\- \[ ] Confirm Permissive input changes

\- \[ ] Confirm analogue current input changes

\- \[ ] Confirm Pickup variable changes above threshold

\- \[ ] Confirm Trip\_Latch works

\- \[ ] Confirm Reset clears Trip\_Latch



\### 10. Final functional test



\- \[ ] Confirm pickup lamp operates above pickup

\- \[ ] Confirm trip lamp operates after trip

\- \[ ] Confirm trip command opens/switches load

\- \[ ] Confirm reset clears trip

\- \[ ] Confirm permissive/block prevents trip

\- \[ ] Confirm Relay Healthy is normally energised

\- \[ ] Confirm Relay Healthy drops out if Opta power/program is stopped



\## Safety Boundary



No mains switching.



No connection to building wiring.



No connection to real CTs, VTs, breakers, substations or electrical installations.



This is a 24 V DC functional demonstrator only.

