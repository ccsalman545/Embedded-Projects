# HC-SR04 ultrasonic distance

![Conceptual HC-SR04 ultrasonic distance pin reference](../../assets/illustrations/sensors/hc-sr04.svg)

> **Quick decision:** choose this for **non-contact distance over a short range**. It communicates over **Pulse timing** and typical Indian retail pricing is **₹70–150** (indicative, checked catalogue range on 17 July 2026; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | Pulse timing |
| Supply | 5 V |
| Typical price in India | ₹70–150 |
| Same-job alternative | VL53L0X / JSN-SR04T |
| Primary technique | Time-of-flight of ~40 kHz ultrasound |

## Reference pinout — labels and functions

> The table uses the signal labels for the reference device/module linked below. Those signal names and functions are exact for that reference; clone breakouts can rearrange physical header order, add regulators, or rename labels. Match the actual silk screen to the linked pinout/datasheet before powering it.

| Pin | Use |
|---|---|
| `VCC` | 5 V |
| `Trig` | 10 µs trigger input |
| `Echo` | 5 V pulse output—level shift for 3.3 V MCU |
| `GND` | return |

## How it works

Time-of-flight of ~40 kHz ultrasound. The module conditions or digitises that physical effect, then exposes it through Pulse timing. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[Pulse timing]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** parking aid, tank level, robot obstacle avoidance. It is a practical choice when non-contact distance over a short range; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the Pulse timing recipe](../PROGRAM_COOKBOOK.md#pulse-timing). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **HC-SR04 ultrasonic distance** | non-contact distance over a short range | Verify calibration, operating range and module variant |
| **VL53L0X / JSN-SR04T** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for parking aid, tank level, robot obstacle avoidance.
- Pulse timing can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [cdn.sparkfun.com](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
