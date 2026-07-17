# Reference and verification policy

## Scope

This library is a **starting reference**, not a wiring authority or a product certification. It was curated on **17 July 2026**. Each entry links the part maker or official board documentation where available. Clone modules often change regulators, pin order and tolerances.

## Price method

INR figures are deliberately **ranges** for Indian hobby-retail modules, not live prices, quotations or recommendations. They exclude/variously include GST, shipping, probes and accessories. Check an Indian supplier at purchase time and record the exact SKU.

## Hardware verification checklist

1. Read the current datasheet and the breakout board silk screen—not just a generic pinout.
2. Confirm supply range, GPIO logic level, maximum current, common ground and boot-strapping pins.
3. Start with a current-limited supply; inspect for shorts; use level shifting where required.
4. Run a bus scan or raw-reading test, then calibrate against a relevant reference.
5. Document firmware version, wiring, ambient conditions, calibration date and uncertainty.

## Safety boundary

Hobby gas, flame, PIR, health and electrical-current modules are **not** certified safety/medical instruments. Use engineered, certified equipment and fail-safe design for fire/gas protection, mains work, medical decisions, payments or any safety-critical action.

## Diagram/image note

The SVG artwork in `assets/illustrations` is original conceptual reference art. It labels common module pins; it is intentionally not a photograph or a manufacturer mechanical drawing.
