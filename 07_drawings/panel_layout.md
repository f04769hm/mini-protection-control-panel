# Panel Layout Draft

## Proposed Physical Layout

Top row:
- 24 V DC power supply
- Fuse / protection
- Supply terminals

Middle row:
- Controller: Opta preferred / Raspberry Pi fallback
- Interface relays
- Current sensor interface

Bottom row:
- Pushbuttons and selector switch
- Indication lamps
- Load / fault branch

## ASCII Layout

+------------------------------------------------------+
| 24 V DC PSU | Fuse | +24 V / 0 V Terminal Blocks     |
+------------------------------------------------------+
| Controller  | Interface Relays | Current Sensor      |
| Opta/Pi     | Trip / Healthy   | Load Measurement    |
+------------------------------------------------------+
| Fault PB | Reset PB | Permissive Switch | Lamps       |
|                                           Load Branch |
+------------------------------------------------------+

## Indication Lamps

Minimum lamp set:

| Lamp | Meaning |
|---|---|
| Supply Healthy | 24 V control supply present |
| Relay Healthy | Controller logic/healthy output present |
| Pickup | Current above pickup threshold |
| Trip | Trip latch operated |
| Blocked | Permissive open or trip blocked |

## Notes

The physical panel should be wired neatly using DIN rail, terminal blocks, ferrules and wire labels where practical.

The aim is not complexity. The aim is a clean, photographable, interview-ready demonstrator.
