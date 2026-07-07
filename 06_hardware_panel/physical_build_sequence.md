\# Physical Build Sequence



\## Rule



Build and test one layer at a time. Do not wire the whole panel in one go.



\## Step 1: Mechanical Layout



\- \[ ] Lay out Opta, PSU, terminals, relays, lamps, pushbuttons, selector and load before wiring

\- \[ ] Confirm selector has PERMIT and BLOCK contacts

\- \[ ] Photograph parts layout

\- \[ ] Mount DIN rail/backboard

\- \[ ] Mount components

\- \[ ] Check there is enough space for wiring and labels



\## Step 2: Power Distribution Only



\- \[ ] Wire PSU + to F1 fuse

\- \[ ] Wire fuse output to +24 V terminal rail

\- \[ ] Wire PSU - to 0 V terminal rail

\- \[ ] Check continuity

\- \[ ] Check for short between +24 V and 0 V

\- \[ ] Power on

\- \[ ] Measure +24 V to 0 V with multimeter

\- \[ ] Power off



\## Step 3: Supply Healthy Lamp



\- \[ ] Wire Supply Healthy lamp from fused +24 V to 0 V

\- \[ ] Power on

\- \[ ] Confirm lamp lights

\- \[ ] Power off



\## Step 4: Opta Power



\- \[ ] Wire W032 from fused +24 V rail to Opta supply +

\- \[ ] Wire W033 from 0 V rail to Opta supply -

\- \[ ] Power on

\- \[ ] Confirm Opta powers up

\- \[ ] Power off



\## Step 5: Inputs and Selector



\- \[ ] Wire Fault/Test PB to I1

\- \[ ] Wire Reset PB to I2

\- \[ ] Wire selector PERMIT contact to I3

\- \[ ] Wire selector BLOCK contact to Blocked lamp

\- \[ ] Confirm selector in PERMIT makes I3 true

\- \[ ] Confirm selector in BLOCK lights Blocked lamp

\- \[ ] Do not connect analogue input yet



\## Step 6: 0–10 V Current Signal



\- \[ ] Confirm physical 0–10 V source

\- \[ ] Power/check 0–10 V source separately

\- \[ ] Measure output with multimeter

\- \[ ] Confirm output cannot exceed 10 V

\- \[ ] Connect signal output to Opta I4

\- \[ ] Connect signal 0 V/common reference correctly

\- \[ ] Monitor analogue value in CODESYS before using trip logic



\## Step 7: Outputs Without Load



\- \[ ] Wire Q2 to healthy relay coil

\- \[ ] Wire healthy relay NO contact to Relay Healthy lamp

\- \[ ] Wire healthy relay NC contact to Unhealthy / Alarm lamp

\- \[ ] Wire Q3 to Pickup lamp

\- \[ ] Wire Q4 to Trip lamp

\- \[ ] Download/monitor program

\- \[ ] Confirm lamps operate logically



\## Step 8: Hardwired Trip Permissive



\- \[ ] Wire selector PERMIT output to Opta Q1 common

\- \[ ] Confirm selector in BLOCK removes +24 V feed from Q1 common

\- \[ ] Confirm selector in PERMIT feeds Q1 common

\- \[ ] Only continue once this is proven with a multimeter



\## Step 9: Trip Relay and Load



\- \[ ] Wire Q1 NO to trip relay coil

\- \[ ] Wire trip relay coil return to 0 V

\- \[ ] Wire load through trip relay NC contact

\- \[ ] Confirm load current is safe

\- \[ ] Test trip operation

\- \[ ] Test reset operation



\## Step 10: Hardware FAT



\- \[ ] Run HT-001 to HT-016 from hardware FAT template

\- \[ ] Record measured results

\- \[ ] Photograph pass conditions

\- \[ ] Save photos in 09\_photos\_video



\## Step 11: Final Pack



\- \[ ] Update terminal schedule if wiring changed

\- \[ ] Update wire numbering plan if wiring changed

\- \[ ] Update limitations page

\- \[ ] Add photos

\- \[ ] Commit final hardware documents

