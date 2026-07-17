# NEO-6M GPS receiver

![Conceptual NEO-6M GPS receiver pin reference](../../assets/illustrations/sensors/neo6m.svg)

> **Quick decision:** choose this for **position, speed and UTC time outdoors**. It communicates over **UART** and typical Indian retail pricing is **₹650–1,400** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | UART |
| Supply | 2.7–3.6 V core; breakout 3–5 V |
| Typical price in India | ₹650–1,400 |
| Same-job alternative | u-blox M8N / phone GNSS |
| Primary technique | GNSS correlation of satellite signals and trilateration |

## Reference pinout — labels and functions

> The table uses the signal labels for the reference device/module linked below. Those signal names and functions are exact for that reference; clone breakouts can rearrange physical header order, add regulators, or rename labels. Match the actual silk screen to the linked pinout/datasheet before powering it.

| Pin | Use |
|---|---|
| `VCC` | breakout power |
| `GND` | return |
| `TX` | NMEA to MCU RX |
| `RX` | config from MCU TX |
| `PPS` | timing pulse |

## How it works

GNSS correlation of satellite signals and trilateration. The module conditions or digitises that physical effect, then exposes it through UART. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[UART]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** vehicle tracker, field logger, clock. It is a practical choice when position, speed and UTC time outdoors; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the UART recipe](../PROGRAM_COOKBOOK.md#uart). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **NEO-6M GPS receiver** | position, speed and UTC time outdoors | Verify calibration, operating range and module variant |
| **u-blox M8N / phone GNSS** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for vehicle tracker, field logger, clock.
- UART can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [content.u-blox.com](https://content.u-blox.com/sites/default/files/NEO-6_DataSheet_%28GPS.G6-HW-09005%29.pdf)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
