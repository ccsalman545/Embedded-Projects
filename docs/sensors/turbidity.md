# Turbidity sensor SEN0189

![Conceptual Turbidity sensor SEN0189 pin reference](../../assets/illustrations/sensors/turbidity.svg)

> **Quick decision:** choose this for **relative water clarity; calibrate with standards**. It communicates over **Analog voltage** and typical Indian retail pricing is **₹750–1,600** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Analog voltage |
| Supply | 5 V |
| Typical price in India | ₹750–1,600 |
| Same-job alternative | nephelometer / TDS sensor |
| Primary technique | Optical scattering/attenuation by suspended particles |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
| `VCC` | 5 V |
| `GND` | return |
| `AO` | analog turbidity voltage |
| `DO` | threshold (module) |

## How it works

Optical scattering/attenuation by suspended particles. The module conditions or digitises that physical effect, then exposes it through Analog voltage. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Analog voltage]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** filter monitor, water experiment. It is a practical choice when relative water clarity; calibrate with standards; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Analog voltage recipe](../PROGRAM_COOKBOOK.md#analog-voltage). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **Turbidity sensor SEN0189** | relative water clarity; calibrate with standards | Verify calibration, operating range and module variant |
| **nephelometer / TDS sensor** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for filter monitor, water experiment.
- Analog voltage can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [wiki.dfrobot.com](https://wiki.dfrobot.com/Turbidity_sensor_SKU__SEN0189)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
