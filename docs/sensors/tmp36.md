# TMP36 analog temperature

![Conceptual TMP36 analog temperature pin reference](../../assets/illustrations/sensors/tmp36.svg)

> **Quick decision:** choose this for **low-voltage analog thermal measurement**. It communicates over **Analog voltage** and typical Indian retail pricing is **₹80–180** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Analog voltage |
| Supply | 2.7–5.5 V |
| Typical price in India | ₹80–180 |
| Same-job alternative | LM35 / MCP9700 |
| Primary technique | Band-gap temperature-to-voltage conversion with offset |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
| `Vs` | power |
| `Vout` | 750 mV at 25°C |
| `GND` | return |

## How it works

Band-gap temperature-to-voltage conversion with offset. The module conditions or digitises that physical effect, then exposes it through Analog voltage. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Analog voltage]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** wearable, battery-operated thermometer. It is a practical choice when low-voltage analog thermal measurement; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Analog voltage recipe](../PROGRAM_COOKBOOK.md#analog-voltage). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **TMP36 analog temperature** | low-voltage analog thermal measurement | Verify calibration, operating range and module variant |
| **LM35 / MCP9700** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for wearable, battery-operated thermometer.
- Analog voltage can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [www.analog.com](https://www.analog.com/en/products/tmp36.html)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
