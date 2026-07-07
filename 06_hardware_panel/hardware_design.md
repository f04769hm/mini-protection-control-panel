# Hardware Design Draft

## Purpose

This document defines the first physical build of the Mini Protection \& Control Panel.

The goal is to create a safe low-voltage 24 V DC demonstrator that shows protection and control workflow: measured current, overcurrent pickup, trip command, hardwired permissive/blocking, relay healthy/watchdog supervision, indication lamps and panel documentation.

## Controller Decision

Selected controller: CODESYS Opta.

Reason: DIN-mount form factor, industrial presentation, 12–24 V DC supply, industrial I/O, relay outputs and IEC 61131-3/CODESYS-style programming. This gives the project a stronger link to industrial control, panel wiring and protection/control engineering than a Raspberry Pi-based build.

Fallback controller: Raspberry Pi 4, but it is reserved for a separate future IEC 61850/GOOSE or OT networking lab. It is not part of this physical panel project.

Reason: already available and suitable for Python-based logic, but requires proper interface circuitry because Raspberry Pi GPIO is 3.3 V logic and must not directly drive 24 V relay coils or panel devices.

No hardware should be purchased until the controller choice and I/O voltage compatibility are confirmed.

No GOOSE, Node-RED, MQTT, pfSense or virtual OT lab is included in this project.

## Control Voltage

Panel/control side: 24 V DC.

Reason: 24 V DC is a common industrial control-panel convention and makes the demonstrator look and behave more like real control equipment than a breadboard/USB-only project.

## Core Functions

1. Supply healthy indication
2. Current measurement input
3. Overcurrent pickup indication
4. IDMT/high-set trip logic
5. Trip relay output opening load circuit
6. Reset pushbutton
7. Permissive/block switch
8. Blocked indication
9. Relay healthy/watchdog indication

## Watchdog / Relay Healthy Concept

A normally energised relay healthy output is used.

The controller holds the healthy output energised while the logic is running correctly. If controller power is lost, the program stops, or the output is not maintained, the healthy relay drops out and the healthy indication is lost.

For the first build, this mimics the fail-safe supervision concept used in protection and control systems.

Limitation: a simple output held continuously high may not detect all software hangs. A stronger future version would use a pulsed heartbeat and missing-pulse detector.

## Trip Circuit Concept

The feeder load is supplied through a trip relay contact.

Normal state:
24 V supply -> fuse -> trip relay contact -> load -> 0 V

Trip state:
The controller operates the trip relay, opening the load circuit and switching off the feeder load.

## Permissive / Blocking Concept

A selector switch provides a permissive/block signal.

Permissive closed:
Fault above pickup can lead to trip.

Permissive open:
Trip is blocked and the blocked indication is shown.

## Safety Boundary

This is an extra-low-voltage demonstrator. It must not switch mains voltage or be connected to any live electrical installation.

The demonstrator is not a protection-class relay, CT measurement chain, certified relay panel or commissioned protection scheme.

