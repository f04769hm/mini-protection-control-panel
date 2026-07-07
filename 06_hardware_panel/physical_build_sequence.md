\# Physical Build Sequence



\## Rule



Build and test one layer at a time. Do not wire the whole panel in one go.



\## Step 1: Mechanical Layout



\- \[ ] Lay out Opta, PSU, terminals, relays, lamps, pushbuttons, selector and load before wiring

\- \[ ] Photograph parts layout

\- \[ ] Mount DIN rail/backboard

\- \[ ] Mount components

\- \[ ] Check there is enough space for wiring and labels



\## Step 2: Power Distribution Only



\- \[ ] Wire PSU + to fuse

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



\- \[ ] Wire Opta supply

\- \[ ] Power on

\- \[ ] Confirm Opta powers up

\- \[ ] Power off



\## Step 5: Inputs



\- \[ ] Wire Fault/Test PB to I1

\- \[ ] Wire Reset PB to I2

\- \[ ] Wire Permissive selector to I3

\- \[ ] Wire 0–10 V signal source to I4 only after checking with multimeter

\- \[ ] Test inputs in CODESYS monitor before outputs are connected



\## Step 6: Outputs Without Load



\- \[ ] Wire Q2 Relay Healthy lamp/relay

\- \[ ] Wire Q3 Pickup lamp

\- \[ ] Wire Q4 Trip lamp

\- \[ ] Download/monitor program

\- \[ ] Confirm lamps operate logically



\## Step 7: Trip Relay and Load



\- \[ ] Wire Q1 to trip relay coil

\- \[ ] Wire trip relay contact in series with load

\- \[ ] Confirm load current is safe

\- \[ ] Test trip operation

\- \[ ] Test reset operation



\## Step 8: Blocked Lamp



\- \[ ] Wire blocked lamp through selector auxiliary/contact

\- \[ ] Confirm blocked lamp changes with selector

\- \[ ] Confirm trip blocked in logic



\## Step 9: Hardware FAT



\- \[ ] Run HT-001 to HT-016 from hardware FAT template

\- \[ ] Record measured results

\- \[ ] Photograph pass conditions

\- \[ ] Save photos in 09\_photos\_video



\## Step 10: Final Pack



\- \[ ] Update terminal schedule if wiring changed

\- \[ ] Update wire numbering plan if wiring changed

\- \[ ] Update limitations page

\- \[ ] Add photos

\- \[ ] Commit final hardware documents

