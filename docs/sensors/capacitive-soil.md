# Capacitive soil moisture sensor

![Conceptual Capacitive soil moisture sensor pin reference](../../assets/illustrations/sensors/capacitive-soil.svg)

> **Quick decision:** choose this for **less-corrosive soil moisture trend**. It communicates over **Analog voltage** and typical Indian retail pricing is **₹120–280** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Analog voltage |
| Supply | 3.3–5.5 V |
| Typical price in India | ₹120–280 |
| Same-job alternative | resistive probe / tensiometer |
| Primary technique | Capacitance changes with soil dielectric constant |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
| `VCC` | power |
| `GND` | return |
| `AOUT` | analog moisture proxy |

## How it works

Capacitance changes with soil dielectric constant. The module conditions or digitises that physical effect, then exposes it through Analog voltage. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Analog voltage]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** irrigation controller, greenhouse node. It is a practical choice when less-corrosive soil moisture trend; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Analog voltage recipe](../PROGRAM_COOKBOOK.md#analog-voltage). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **Capacitive soil moisture sensor** | less-corrosive soil moisture trend | Verify calibration, operating range and module variant |
| **resistive probe / tensiometer** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for irrigation controller, greenhouse node.
- Analog voltage can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [wiki.dfrobot.com](https://wiki.dfrobot.com/Capacitive_Soil_Moisture_Sensor_SKU_SEN0193)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
