\# First Upload Test Plan



\## Purpose



This plan defines the first safe test of the CODESYS Opta logic before the panel is fully wired.



The aim is to prove the program runs, variables behave correctly and outputs are understood before connecting relays, lamps or load circuits.



\## Test Setup



Hardware connected:



\- CODESYS Opta

\- 24 V DC supply, if required for Opta operation

\- Programming connection to laptop



Hardware not connected:



\- Trip relay

\- Load circuit

\- Panel lamps

\- External current sensor

\- Any mains voltage

\- Any real electrical installation



\## Test 1: Compile



Expected result:



\- Project builds without syntax errors



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 2: Download to Opta



Expected result:



\- Program downloads successfully

\- PLC/runtime enters run mode



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 3: Monitor Relay Healthy



Expected result:



\- Relay\_Healthy variable is TRUE while program is running



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 4: Below Pickup



Input condition:



\- Current\_Input\_V = 0.0 V or simulated equivalent



Expected result:



\- Current\_A = 0 A

\- Pickup = FALSE

\- Trip\_Latch = FALSE

\- Trip\_Command = FALSE



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 5: Above Pickup



Input condition:



\- Current\_Input\_V = 1.0 V or simulated equivalent



Expected result:



\- Current\_A = 600 A

\- Pickup = TRUE

\- IDMT progress increases

\- Trip eventually operates if permissive is true



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 6: Permissive Block



Input condition:



\- Permissive = FALSE

\- Current\_Input\_V above pickup



Expected result:



\- Pickup may be TRUE

\- Trip\_Command remains FALSE

\- Operate\_Progress resets or remains zero



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 7: Reset



Input condition:



\- Trip\_Latch = TRUE

\- Reset\_PB = TRUE



Expected result:



\- Trip\_Latch resets

\- Trip\_Command becomes FALSE

\- Trip\_Lamp becomes FALSE

\- Operate\_Progress resets



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Test 8: High-Set



Input condition:



\- Current\_Input\_V = 8.5 V or simulated equivalent



Expected result:



\- Current\_A = approximately 5100 A

\- High-set timer runs

\- Trip\_Latch operates after approximately 50 ms



Result:



\- \[ ] Pass

\- \[ ] Fail



Notes:



\## Pass Criteria



The first upload is successful when:



\- the project compiles

\- the program downloads

\- PLC/runtime runs

\- key variables can be monitored

\- pickup, trip, reset and permissive logic behave as expected



Only after this should physical lamps, relays and load circuits be connected.

