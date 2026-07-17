# YF-S201 water-flow sensor

![Conceptual YF-S201 water-flow sensor pin reference](../../assets/illustrations/sensors/yf-s201-flow.svg)

> **Quick decision:** choose this for **inexpensive water-flow totalisation after calibration**. It communicates over **Pulse timing** and typical Indian retail pricing is **₹250–600** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Pulse timing |
| Supply | 5–18 V |
| Typical price in India | ₹250–600 |
| Same-job alternative | industrial flow meter / ultrasonic flow sensor |
| Primary technique | Magnetised turbine and Hall switch generate pulses proportional to flow |

## Reference pinout — labels and functions

> The table uses the signal labels for the reference device/module linked below. Those signal names and functions are exact for that reference; clone breakouts can rearrange physical header order, add regulators, or rename labels. Match the actual silk screen to the linked pinout/datasheet before powering it.

| Pin | Use |
|---|---|
| `Red` | supply |
| `Black` | ground |
| `Yellow` | open-collector pulse output—use a pull-up compatible with MCU GPIO |

## How it works

Magnetised turbine and Hall switch generate pulses proportional to flow. The module conditions or digitises that physical effect, then exposes it through Pulse timing. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Pulse timing]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** water dispenser, irrigation totaliser, leak trend. It is a practical choice when inexpensive water-flow totalisation after calibration; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Pulse timing recipe](../PROGRAM_COOKBOOK.md#pulse-timing). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **YF-S201 water-flow sensor** | inexpensive water-flow totalisation after calibration | Verify calibration, operating range and module variant |
| **industrial flow meter / ultrasonic flow sensor** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for water dispenser, irrigation totaliser, leak trend.
- Pulse timing can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [components101.com](https://components101.com/sensors/yf-s201-water-flow-measurement-sensor)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
