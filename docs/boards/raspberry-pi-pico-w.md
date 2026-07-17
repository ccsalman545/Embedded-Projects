# Raspberry Pi Pico W

![Conceptual Raspberry Pi Pico W board pin reference](../../assets/illustrations/boards/raspberry-pi-pico-w.svg)

> **Role:** MicroPython wireless edge node. Typical Indian retail range: **₹650–1,200** (indicative on 17 July 2026, not a live quote).

| Property | Reference |
|---|---|
| Controller | RP2040 + Wi‑Fi, 3.3 V |
| I/O summary | 26 GPIO; ADC, UART, I²C, SPI, PWM, PIO |
| Logic level | Check the board documentation; many pins are 3.3 V-only |
| Alternative | ESP32 / Pico |

## Key pins and connectors

| Pin / connector | Use |
|---|---|
| `Micro-USB` | power/programming |
| `VSYS/3V3_OUT/GND` | power |
| `GPIO map matches Pico` | See board documentation |
| `wireless uses CYW43439` | See board documentation |

```mermaid
flowchart LR
  USB[USB / power] --> MCU[Microcontroller board]
  MCU --> GPIO[GPIO / ADC / PWM]
  MCU --> Buses[I²C · SPI · UART]
  Buses --> Sensors[Sensors & modules]
  GPIO --> Actuators[Drivers & actuators]
```

## Applications, technique and selection

The board executes firmware stored in its controller and uses digital/analog peripherals to sample sensors and drive outputs. Choose it for **MicroPython wireless edge node**: its processor, voltage domain, memory, connectivity and physical size determine whether it fits. Typical applications include data loggers, control panels, robotics and connected sensor nodes.

## Three first programs, output and inference

1. [Blink / GPIO smoke test](../PROGRAM_COOKBOOK.md#blink-gpio-smoke-test): LED changes every second — proves upload, clock and output pin.
2. [I²C scanner](../PROGRAM_COOKBOOK.md#i2c-scanner): serial output lists responding addresses — proves shared-bus wiring.
3. [Filtered telemetry and alarm](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm): serial readings and state — proves the acquisition-to-decision loop.

**Inference:** passing these tests does not establish voltage compatibility or sensor accuracy. Confirm common ground, logic levels, current budget and exact pin multiplexing before expansion.

## Comparison and trade-offs

| Board | Best when | Trade-off |
|---|---|---|
| **Raspberry Pi Pico W** | MicroPython wireless edge node | Check its exact variant, USB interface and voltage limits |
| **ESP32 / Pico** | requirements differ in wireless capability, speed, I/O or power | requires a different toolchain or wiring plan |

**Advantages:** popular tools/tutorials; flexible interfaces; fast iteration.

**Disadvantages:** development boards are not automatically rugged, low-power or electrically protected products; add regulator, protection, enclosure and driver circuitry where needed.

## Verification source

- Official documentation: [www.raspberrypi.com](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- [Reference policy](../REFERENCE_POLICY.md)
