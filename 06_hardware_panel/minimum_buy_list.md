\# Minimum Buy List



\## Purpose



This list records only the items that may need to be bought personally if they cannot be sourced through proper work/lab channels.



The goal is to keep personal spend low and avoid buying unnecessary hardware.



\## Buy Only If Not Available



| Item | Quantity | Must Check |

|---|---:|---|

| Momentary pushbutton | 2 | Suitable for 24 V panel use |

| Maintained 2-position selector switch | 1 | Suitable for 24 V panel use |

| Fuse holder + small DC fuse | 1 | Suitable for 24 V DC demonstrator circuit |

| 24 V load lamp or suitable resistor | 1 | Current within PSU, fuse and relay contact ratings |

| 0–10 V signal generator/current simulator | 1 | Output limited to 0–10 V, checked with multimeter before Opta connection |



\## Do Not Buy Yet



| Item | Reason |

|---|---|

| Real protection relay | Scope creep and compatibility risk |

| Opta expansion module | Base Opta I/O is enough |

| Raspberry Pi accessories | Pi is not part of this build |

| Current sensor | Use 0–10 V simulation first |

| SCADA hardware | Not part of v1 |

| Networking gear | Not part of v1 |

| Extra lamps/switches | Avoid unnecessary output complexity |



\## 0–10 V Signal Requirement



The current input for version 1 is simulated as:



Current\_A = Input\_V × 600



Therefore:



| Voltage | Simulated Current |

|---:|---:|

| 0.5 V | 300 A pickup |

| 1.0 V | 600 A / 2x pickup |

| 2.5 V | 1500 A / 5x pickup |

| 5.0 V | 3000 A / 10x pickup |

| 6.67 V | 4000 A high-set |
| 8.33 V | 5000 A above high-set test point |



The signal source must never exceed 10 V into the Opta analogue input.

