# DHT11 temperature & humidity

![Conceptual DHT11 temperature & humidity pin reference](../../assets/illustrations/sensors/dht11.svg)

> **Quick decision:** choose this for **low-cost room climate indication**. It communicates over **Single-wire digital** and typical Indian retail pricing is **₹70–140** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Single-wire digital |
| Supply | 3.3–5 V |
| Typical price in India | ₹70–140 |
| Same-job alternative | DHT22 / SHT31 |
| Primary technique | Polymer capacitive humidity element plus NTC temperature measurement |

## Reference pinout — labels and functions

> The table uses the signal labels for the reference device/module linked below. Those signal names and functions are exact for that reference; clone breakouts can rearrange physical header order, add regulators, or rename labels. Match the actual silk screen to the linked pinout/datasheet before powering it.

| Pin | Use |
|---|---|
| `VCC` | power |
| `DATA` | digital data |
| `NC` | unused |
| `GND` | return |

## How it works

Polymer capacitive humidity element plus NTC temperature measurement. The module conditions or digitises that physical effect, then exposes it through Single-wire digital. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Single-wire digital]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** weather node, incubator, classroom logger. It is a practical choice when low-cost room climate indication; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Single-wire digital recipe](../PROGRAM_COOKBOOK.md#single-wire-digital). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **DHT11 temperature & humidity** | low-cost room climate indication | Verify calibration, operating range and module variant |
| **DHT22 / SHT31** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for weather node, incubator, classroom logger.
- Single-wire digital can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [www.aosong.com](https://www.aosong.com/en/products-22.html)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
