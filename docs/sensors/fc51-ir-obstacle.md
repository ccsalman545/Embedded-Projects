# FC-51 IR obstacle sensor

![Conceptual FC-51 IR obstacle sensor pin reference](../../assets/illustrations/sensors/fc51-ir-obstacle.svg)

> **Quick decision:** choose this for **simple short-range obstacle indication**. It communicates over **Digital threshold** and typical Indian retail pricing is **₹40–100** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Digital threshold |
| Supply | 3.3–5 V |
| Typical price in India | ₹40–100 |
| Same-job alternative | HC-SR04 / VL53L0X |
| Primary technique | Modulated IR LED and phototransistor reflection with an LM393 comparator |

## Reference pinout — labels and functions

> The table uses the signal labels for the reference device/module linked below. Those signal names and functions are exact for that reference; clone breakouts can rearrange physical header order, add regulators, or rename labels. Match the actual silk screen to the linked pinout/datasheet before powering it.

| Pin | Use |
|---|---|
| `VCC` | power |
| `GND` | return |
| `OUT` | active-low object detect |

## How it works

Modulated IR LED and phototransistor reflection with an LM393 comparator. The module conditions or digitises that physical effect, then exposes it through Digital threshold. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Digital threshold]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** line/obstacle robot, object counter demo. It is a practical choice when simple short-range obstacle indication; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Digital threshold recipe](../PROGRAM_COOKBOOK.md#digital-threshold). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **FC-51 IR obstacle sensor** | simple short-range obstacle indication | Verify calibration, operating range and module variant |
| **HC-SR04 / VL53L0X** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for line/obstacle robot, object counter demo.
- Digital threshold can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [components101.com](https://components101.com/sensors/ir-sensor-module)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
