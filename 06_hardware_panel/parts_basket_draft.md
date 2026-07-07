# Parts Basket Draft

This is a draft only. Do not buy until controller choice and voltage compatibility are confirmed.

## Already Available / To Confirm

| Item | Status |
|---|---|
| Raspberry Pi 4 | Available |
| Arduino Opta | To confirm / preferred if available cheaply |
| Windows laptop | Available |
| GitHub repo | Available |
| Python software FAT | Complete |

## Required Panel Hardware

| Item | Purpose | Notes |
|---|---|---|
| 24 V DC DIN rail power supply | Panel/control supply | Keep demonstrator extra-low-voltage |
| DIN rail / backboard / enclosure | Physical mounting | Main thing that makes it look like a control panel |
| Terminal blocks | Clean wiring and documentation | Numbered terminals preferred |
| Ferrules and crimper | Proper wire termination | Confirm if already owned |
| Wire labels / marker sleeves | Panel documentation | Helps match wiring to I/O list |
| 24 V indicator lamps | Supply, healthy, pickup, trip, blocked | 5 lamps is enough |
| Pushbuttons | Fault/test and reset | Momentary type |
| Selector switch | Permissive/block | Maintained type |
| Interface relay | Trip relay output | Must match controller output/driver |
| Interface relay | Relay healthy/watchdog | Normally energised healthy concept |
| Fuse holder / small DC fuse | Basic circuit protection | For 24 V panel supply/load |
| Load lamp or resistor | Feeder load representation | Must be sized safely for supply |
| Current sensor | Current measurement | Choice depends on controller |
| Wire | Panel wiring | Use sensible colours if available |

## Important Compatibility Checks

1. Controller output voltage/current must match relay/input module requirements.
2. Raspberry Pi GPIO is 3.3 V and cannot directly drive 24 V devices.
3. Relay coils/modules must be compatible with the chosen controller or driven through an interface stage.
4. Current sensor output must be readable by the chosen controller.
5. Load current must stay within current-sensor rating and power-supply rating.
6. All work stays extra-low-voltage; no mains switching.

## Buying Rule

Spend money on panel realism first: DIN rail, terminals, ferrules, labels, lamps and switches.

Do not buy:
- used protection relay
- relay test set
- SCADA hardware
- protocol/networking extras
- anything for GOOSE/IEC 61850 in this project
