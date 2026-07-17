#!/usr/bin/env python3
"""Generate the maintained embedded reference catalogue from curated records."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TODAY = "17 July 2026"

# name, slug, interface, voltage, pins, technique, use, applications, price, compare, source
SENSORS = [
("DHT11 temperature & humidity", "dht11", "Single-wire digital", "3.3–5 V", "VCC: power; DATA: digital data; NC: unused; GND: return", "Polymer capacitive humidity element plus NTC temperature measurement", "low-cost room climate indication", "weather node, incubator, classroom logger", "₹70–140", "DHT22 / SHT31", "https://www.aosong.com/en/products-22.html"),
("DHT22 / AM2302", "dht22", "Single-wire digital", "3.3–6 V", "VCC: power; DATA: digital data; NC: unused; GND: return", "Capacitive humidity and band-gap temperature sensing", "better range and accuracy than DHT11", "greenhouse, HVAC logger, storage monitor", "₹220–450", "SHT31 / BME280", "https://www.aosong.com/en/products-22.html"),
("SHT31 temperature & humidity", "sht31", "I²C", "2.4–5.5 V", "VIN: power; GND: return; SDA: I²C data; SCL: I²C clock; ADR: address select", "Digital capacitive humidity sensor with band-gap temperature sensor", "repeatable environmental measurements", "HVAC, weather station, museum logger", "₹450–850", "BME280 / AHT20", "https://sensirion.com/products/catalog/SHT31-DIS"),
("BME280 environmental", "bme280", "I²C / SPI", "1.71–3.6 V core; most breakouts 3–5 V", "VIN: power; GND: return; SDA/SDI: data; SCL/SCK: clock; CS: SPI select; SDO: address/MISO", "MEMS pressure, capacitive humidity and temperature sensing", "temperature, RH and barometric pressure in one part", "portable weather station, altitude trend, IoT", "₹280–650", "BMP280 / SHT31", "https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors/bme280/"),
("BMP280 barometric pressure", "bmp280", "I²C / SPI", "1.71–3.6 V core; breakout varies", "VIN: power; GND: return; SDA/SDI: data; SCL/SCK: clock; CS: select; SDO: address/MISO", "Piezoresistive MEMS absolute pressure cell", "pressure and relative altitude trend", "altimeter, drone telemetry, weather node", "₹180–450", "BME280 / MPL3115A2", "https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp280/"),
("DS18B20 waterproof temperature", "ds18b20", "1-Wire", "3.0–5.5 V", "VDD (red): power; DQ (yellow): 1-Wire data; GND (black): return; use 4.7 kΩ pull-up on DQ", "Band-gap temperature sensor with on-chip ADC", "robust, addressable temperature probes", "aquarium, solar heater, cold-chain logger", "₹120–260", "NTC probe / TMP117", "https://www.analog.com/en/products/ds18b20.html"),
("LM35 analog temperature", "lm35", "Analog voltage", "4–30 V", "Vs: power; Vout: 10 mV/°C output; GND: return", "Precision band-gap temperature-to-voltage conversion", "simple calibrated analog temperature", "thermostat, lab experiment, battery thermal alarm", "₹45–120", "TMP36 / DS18B20", "https://www.ti.com/product/LM35"),
("TMP36 analog temperature", "tmp36", "Analog voltage", "2.7–5.5 V", "Vs: power; Vout: 750 mV at 25°C; GND: return", "Band-gap temperature-to-voltage conversion with offset", "low-voltage analog thermal measurement", "wearable, battery-operated thermometer", "₹80–180", "LM35 / MCP9700", "https://www.analog.com/en/products/tmp36.html"),
("NTC thermistor module", "ntc-thermistor", "Analog voltage", "3.3–5 V", "VCC: power; GND: return; AO: divider voltage; DO: threshold comparator output", "Negative-temperature-coefficient semiconductor resistance", "fast, inexpensive thermal thresholding", "3D printer, battery pack, appliance", "₹40–100", "DS18B20 / PT100", "https://www.murata.com/en-global/products/thermistor/ntc"),
("MQ-2 smoke / LPG gas", "mq2", "Analog + digital threshold", "5 V (heater)", "VCC: 5 V heater; GND: return; AO: analog concentration proxy; DO: comparator alarm", "Heated SnO₂ chemiresistor changes resistance in reducing gases", "low-cost combustible-gas alarm experiments", "smoke alarm demonstrator, LPG leak alert", "₹90–180", "MQ-135 / electrochemical gas sensor", "https://www.winsen-sensor.com/product/mq-2.html"),
("MQ-135 air-quality gas", "mq135", "Analog + digital threshold", "5 V (heater)", "VCC: 5 V heater; GND: return; AO: analog resistance proxy; DO: threshold", "Heated SnO₂ chemiresistor responsive to several gases", "qualitative ventilation/air-change indicator", "classroom air monitor, exhaust alert", "₹100–220", "SGP30 / CCS811", "https://www.winsen-sensor.com/product/mq-135.html"),
("CCS811 eCO₂ / TVOC", "ccs811", "I²C", "1.8–3.6 V", "VIN: power; GND: return; SDA: data; SCL: clock; nWAKE: wake; nINT: interrupt; nRST: reset", "Metal-oxide gas sensing with on-chip algorithm", "relative indoor air-quality trend", "ventilation automation, desk monitor", "₹650–1,300", "SGP30 / ENS160", "https://www.sciosense.com/products/environmental-sensors/ccs811/"),
("SGP30 eCO₂ / TVOC", "sgp30", "I²C", "1.62–1.98 V core; breakout regulated", "VIN: breakout power; GND: return; SDA: data; SCL: clock", "MOx gas pixels with humidity-compensated IAQ algorithm", "compact air-quality trend", "smart home, purifier control", "₹800–1,600", "CCS811 / ENS160", "https://sensirion.com/products/catalog/SGP30"),
("PMS5003 particulate matter", "pms5003", "UART", "5 V", "VCC: 5 V; GND: return; TX: sensor data to MCU RX; RX: control from MCU TX; SET: sleep; RESET: reset", "Laser scattering particle counter", "PM1/PM2.5/PM10 mass-concentration estimate", "air-quality station, filter monitor", "₹1,500–3,000", "SDS011 / SEN55", "https://www.plantower.com/en/content/?108.html"),
("SDS011 particulate matter", "sds011", "UART", "5 V", "5V: power; GND: return; TXD: data to MCU RX; RXD: command input", "Laser light-scattering particle measurement", "PM2.5 and PM10 monitoring", "outdoor AQ node, DIY purifier feedback", "₹1,600–3,200", "PMS5003 / SEN55", "https://www.inovafitness.com/en/a/laser-pm2-5-sensor-sds011.html"),
("BH1750 ambient light", "bh1750", "I²C", "2.4–3.6 V core; breakout often 3–5 V", "VCC: power; GND: return; SDA: data; SCL: clock; ADDR: I²C address select", "Photodiode with spectral response and digital lux conversion", "ambient illuminance in lux", "auto-dimming, solar logger, lighting control", "₹100–250", "VEML7700 / LDR", "https://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/light/bh1750fvi-e.pdf"),
("LDR photoresistor module", "ldr", "Analog + digital threshold", "3.3–5 V", "VCC: power; GND: return; AO: light-dependent divider voltage; DO: threshold", "Photoconductive CdS resistance changes with illumination", "very low-cost light/dark detection", "night light, line follower calibration", "₹30–80", "BH1750 / photodiode", "https://learn.adafruit.com/photocells"),
("VEML7700 ambient light", "veml7700", "I²C", "2.5–3.6 V", "VIN: power; GND: return; SDA: data; SCL: clock", "Silicon photodiode ALS with digital integration", "wide-range calibrated light level", "display dimming, daylight harvesting", "₹350–750", "BH1750 / TSL2591", "https://www.vishay.com/docs/84286/veml7700.pdf"),
("TSL2591 light sensor", "tsl2591", "I²C", "2.7–3.6 V", "VIN: power; GND: return; SDA: data; SCL: clock; INT: interrupt", "Dual photodiodes (visible + IR) with programmable gain", "very low to bright-light measurement", "astronomy logger, greenhouse, lux meter", "₹650–1,300", "VEML7700 / BH1750", "https://ams-osram.com/products/sensor-solutions/ambient-light-color-spectral-proximity-sensors/ams-tsl2591-digital-light-sensor"),
("HC-SR04 ultrasonic distance", "hc-sr04", "Pulse timing", "5 V", "VCC: 5 V; Trig: 10 µs trigger input; Echo: 5 V pulse output—level shift for 3.3 V MCU; GND: return", "Time-of-flight of ~40 kHz ultrasound", "non-contact distance over a short range", "parking aid, tank level, robot obstacle avoidance", "₹70–150", "VL53L0X / JSN-SR04T", "https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf"),
("VL53L0X laser ToF distance", "vl53l0x", "I²C", "2.6–3.5 V", "VIN: breakout power; GND: return; SDA: data; SCL: clock; XSHUT: shutdown; GPIO1: interrupt", "940 nm VCSEL time-of-flight ranging", "compact optical distance measurement", "gesture range, robot, liquid level", "₹500–1,000", "HC-SR04 / VL53L1X", "https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html"),
("Sharp GP2Y0A21 IR distance", "gp2y0a21", "Analog voltage", "4.5–5.5 V", "VCC: power; GND: return; Vo: nonlinear analog distance voltage", "Triangulation of reflected modulated infrared light", "short-range distance with simple ADC", "robot wall detection, object sorter", "₹700–1,400", "HC-SR04 / VL53L0X", "https://global.sharp/products/device/lineup/data/pdf/datasheet/gp2y0a21yk_e.pdf"),
("PIR motion sensor HC-SR501", "pir", "Digital threshold", "4.5–20 V", "VCC: power; OUT: logic motion output; GND: return; sensitivity/time potentiometers on module", "Pyroelectric differential IR sensing with Fresnel lens", "human/animal motion, not presence", "security light, occupancy trigger", "₹80–180", "mmWave radar / microwave Doppler", "https://www.mpja.com/download/31227sc.pdf"),
("RCWL-0516 microwave motion", "rcwl0516", "Digital threshold", "4–28 V", "VIN: power; GND: return; OUT: motion logic output; 3V3: regulated output; CDS: light inhibit", "Microwave Doppler radar detects motion", "motion detection through some non-metallic covers", "hidden occupancy trigger, automatic door", "₹70–180", "PIR / mmWave presence", "https://components101.com/sensors/rcwl-0516-microwave-doppler-radar-sensor"),
("Reed switch magnetic door sensor", "reed-switch", "Digital contact", "3.3–5 V with pull-up", "One lead: MCU input; other lead: GND (or VCC); use pull-up/pull-down; module: VCC/GND/DO", "Magnetically actuated sealed ferrous contacts", "reliable open/close state", "door alarm, limit switch, bicycle speed", "₹25–100", "Hall sensor / optical endstop", "https://standexelectronics.com/products/technology/reed-switches/"),
("A3144 Hall-effect sensor", "a3144", "Digital open collector", "4.5–24 V", "VCC: power; GND: return; OUT: open-collector output, add pull-up", "Hall effect magnetic field threshold switch", "contactless magnet detection", "RPM counter, endstop, wheel speed", "₹40–120", "Reed switch / AS5600", "https://www.allegromicro.com/en/products/sense/switches-and-latches/a3141-2-3-4"),
("AS5600 magnetic encoder", "as5600", "I²C / analog / PWM", "3.0–5.5 V", "VCC: power; GND: return; SDA: data; SCL: clock; OUT: analog/PWM angle; DIR: direction", "Contactless Hall-array magnetic angle measurement", "absolute rotary position", "knob, motor position, robot joint", "₹300–750", "potentiometer / incremental encoder", "https://ams-osram.com/products/sensor-solutions/position-sensors/ams-as5600-position-sensor"),
("MPU6050 IMU", "mpu6050", "I²C", "2.375–3.46 V core; breakout regulated", "VCC: power; GND: return; SDA: data; SCL: clock; INT: data-ready; AD0: address select", "MEMS capacitive accelerometer plus vibrating-mass gyroscope", "linear acceleration and angular-rate sensing", "tilt alarm, balancing robot, gesture input", "₹180–450", "ICM-20948 / BMI160", "https://invensense.tdk.com/products/motion-tracking/6-axis/mpu-6050/"),
("ADXL345 accelerometer", "adxl345", "I²C / SPI", "1.8–3.6 V", "VCC: power; GND: return; SDA/SDI: data; SCL/SCLK: clock; CS: select; SDO: address/MISO; INT1/2: interrupts", "MEMS capacitive 3-axis acceleration", "low-power acceleration, tap and free-fall events", "activity tracker, impact logger, tilt switch", "₹250–650", "MPU6050 / LIS3DH", "https://www.analog.com/en/products/adxl345.html"),
("LIS3DH accelerometer", "lis3dh", "I²C / SPI", "1.71–3.6 V", "VDD: power; GND: return; SDA/SDI: data; SCL/SCK: clock; CS: select; SDO: address; INT1/2: interrupts", "MEMS capacitive 3-axis acceleration", "low-power motion and orientation events", "wearable, shipping shock recorder", "₹250–650", "ADXL345 / MPU6050", "https://www.st.com/en/mems-and-sensors/lis3dh.html"),
("HMC5883L magnetometer", "hmc5883l", "I²C", "2.16–3.6 V", "VCC: power; GND: return; SDA: data; SCL: clock; DRDY: data-ready", "Anisotropic magnetoresistive 3-axis field sensing", "magnetic heading after calibration", "compass, direction logger", "₹180–450", "QMC5883L / LIS3MDL", "https://www.analog.com/en/products/hmc5883l.html"),
("QMC5883L magnetometer", "qmc5883l", "I²C", "2.16–3.6 V", "VCC: power; GND: return; SDA: data; SCL: clock; DRDY: data-ready", "3-axis magnetic-field sensor with digital compensation", "low-cost compass heading after calibration", "navigation robot, compass display", "₹120–320", "HMC5883L / LIS3MDL", "https://qstcorp.com/en_magnetic_sensor/"),
("NEO-6M GPS receiver", "neo6m", "UART", "2.7–3.6 V core; breakout 3–5 V", "VCC: breakout power; GND: return; TX: NMEA to MCU RX; RX: config from MCU TX; PPS: timing pulse", "GNSS correlation of satellite signals and trilateration", "position, speed and UTC time outdoors", "vehicle tracker, field logger, clock", "₹650–1,400", "u-blox M8N / phone GNSS", "https://content.u-blox.com/sites/default/files/NEO-6_DataSheet_%28GPS.G6-HW-09005%29.pdf"),
("MAX30102 pulse-oximeter", "max30102", "I²C", "1.8 V core; breakout 3.3–5 V", "VIN: breakout power; GND: return; SDA: data; SCL: clock; INT: FIFO interrupt", "Red/IR photoplethysmography measures pulsatile absorption", "educational heart-rate / SpO₂ estimation—not diagnostic", "fitness demo, signal-processing lab", "₹250–650", "MAX30105 / dedicated medical device", "https://www.analog.com/en/products/max30102.html"),
("MAX30105 particle / optical", "max30105", "I²C", "1.8 V core; breakout 3.3–5 V", "VIN: power; GND: return; SDA: data; SCL: clock; INT: interrupt", "Multi-LED reflected-light photometry", "gesture, proximity and experimental pulse waveform", "hand-wash timer, optical experiment", "₹450–950", "APDS9960 / MAX30102", "https://www.analog.com/en/products/max30105.html"),
("Soil moisture probe", "soil-moisture", "Analog + digital threshold", "3.3–5 V", "VCC: power; GND: return; AO: wetness divider voltage; DO: threshold output", "Resistive conductivity measurement between exposed electrodes", "rough soil wet/dry indication; corrodes if powered continuously", "plant alert, irrigation demonstrator", "₹50–130", "capacitive soil sensor", "https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide"),
("Capacitive soil moisture sensor", "capacitive-soil", "Analog voltage", "3.3–5.5 V", "VCC: power; GND: return; AOUT: analog moisture proxy", "Capacitance changes with soil dielectric constant", "less-corrosive soil moisture trend", "irrigation controller, greenhouse node", "₹120–280", "resistive probe / tensiometer", "https://wiki.dfrobot.com/Capacitive_Soil_Moisture_Sensor_SKU_SEN0193"),
("Rain / raindrop module", "rain", "Analog + digital threshold", "3.3–5 V", "VCC: power; GND: return; AO: plate conductivity voltage; DO: threshold", "Water bridges conductive tracks, changing resistance", "detect rain/water presence; plate corrodes", "rain alarm, window closer demonstrator", "₹60–150", "tipping-bucket rain gauge", "https://components101.com/sensors/rain-sensor-module"),
("Water level float switch", "float-switch", "Digital contact", "3.3–5 V with pull-up", "COM: common; NO/NC: contact state (orientation dependent); module: VCC/GND/DO", "Buoyant magnet actuates a reed switch", "simple point-level detection", "tank empty/full alarm, sump protection", "₹60–180", "ultrasonic / pressure transducer", "https://standexelectronics.com/products/technology/liquid-level-sensors/"),
("Turbidity sensor SEN0189", "turbidity", "Analog voltage", "5 V", "VCC: 5 V; GND: return; AO: analog turbidity voltage; DO: threshold (module)", "Optical scattering/attenuation by suspended particles", "relative water clarity; calibrate with standards", "filter monitor, water experiment", "₹750–1,600", "nephelometer / TDS sensor", "https://wiki.dfrobot.com/Turbidity_sensor_SKU__SEN0189"),
("TDS / conductivity module", "tds", "Analog voltage", "3.3–5.5 V", "VCC: power; GND: return; AOUT: conditioned probe signal; probe: conductivity electrodes", "AC conductivity measurement estimates dissolved ionic solids", "water conductivity/TDS trend with temperature compensation", "hydroponics, RO filter trend", "₹650–1,500", "EC meter / pH sensor", "https://wiki.dfrobot.com/Gravity__Analog_TDS_Sensor___Meter_For_Arduino_SKU__SEN0244"),
("pH electrode interface", "ph", "Analog voltage", "5 V", "VCC: power; GND: return; PO/AO: high-impedance conditioned pH voltage; BNC: probe", "Glass electrode electrochemical potential versus reference", "pH after two/three-point calibration", "aquaponics, water chemistry lab", "₹1,200–3,000", "industrial pH transmitter", "https://wiki.dfrobot.com/PH_meter_SKU__SEN0161_"),
("HX711 load-cell ADC", "hx711", "Two-wire synchronous", "2.6–5.5 V", "VCC: power; GND: return; DT/DOUT: serial data; SCK: clock; E+/E−: excitation; A+/A−: load cell", "24-bit differential ADC measures strain-gauge Wheatstone bridge", "weight/force after tare and calibration", "kitchen scale, hopper weight, force test", "₹120–300 (ADC); load cell extra", "NAU7802 / industrial indicator", "https://www.aviaic.com/product/710.html"),
("Load cell strain gauge", "load-cell", "Bridge analog (via HX711)", "typically 5–10 V excitation", "E+: bridge excitation +; E−: excitation −; S+/A+: signal +; S−/A−: signal −", "Metal-foil strain gauges change resistance under deformation", "force or mass with stable mechanics and calibration", "weighing scale, material test rig", "₹300–1,500", "FSR / pressure sensor", "https://www.omega.com/en-us/resources/load-cells"),
("FSR force-sensitive resistor", "fsr", "Analog voltage", "3.3–5 V divider", "Two terminals: place in voltage divider; module VCC/GND/AO if supplied", "Polymer thick-film resistance falls with applied force", "qualitative touch/force detection, not precision weighing", "drum pad, seat occupancy, grip input", "₹250–700", "load cell / capacitive force sensor", "https://www.interlinkelectronics.com/fsr-400-series"),
("Flex sensor", "flex-sensor", "Analog voltage", "3.3–5 V divider", "Two terminals: variable resistor; use a fixed resistor divider into ADC", "Conductive ink resistance changes when bent", "bend-angle proxy after per-device calibration", "data glove, posture demo, soft robot", "₹500–1,200", "IMU / rotary encoder", "https://www.spectrasymbol.com/flex-sensor"),
("Sound sensor MAX9814", "max9814", "Analog voltage", "2.7–5.5 V", "VDD: power; GND: return; OUT: biased audio waveform; GAIN/AR: gain controls where exposed", "Electret microphone with automatic-gain amplifier", "audio amplitude/envelope—not calibrated dB without calibration", "clap detector, sound-reactive light, recorder front end", "₹220–550", "INMP441 / SPL meter", "https://www.analog.com/en/products/max9814.html"),
("INMP441 I²S microphone", "inmp441", "I²S digital audio", "1.62–3.63 V", "VDD: 3.3 V; GND: return; SCK/BCLK: bit clock; WS/LRCLK: word select; SD: audio data; L/R: channel select", "MEMS capacitive microphone with sigma-delta ADC", "digital audio capture with known sample format", "voice activity, audio logger, FFT visualizer", "₹250–650", "MAX9814 / PDM microphone", "https://invensense.tdk.com/products/digital/inmp441/"),
("Flame sensor module", "flame", "Analog + digital threshold", "3.3–5 V", "VCC: power; GND: return; AO: IR intensity proxy; DO: threshold", "Silicon photodiode detects flickering near-IR/visible flame radiation", "flame indication in controlled demos; not fire-safety certified", "robot fire-finding demo, burner monitor", "₹70–170", "UV flame detector / smoke alarm", "https://components101.com/sensors/flame-sensor-module"),
("UV sensor VEML6075", "veml6075", "I²C", "2.5–3.6 V", "VIN: power; GND: return; SDA: data; SCL: clock", "UVA/UVB photodiodes with compensated UV-index calculation", "relative UV index for outdoor projects", "sun exposure logger, UV lamp check", "₹800–1,600", "VEML6070 / calibrated radiometer", "https://www.vishay.com/docs/84304/veml6075.pdf"),
("APDS9960 gesture / colour", "apds9960", "I²C", "2.4–3.6 V", "VIN: power; GND: return; SDA: data; SCL: clock; INT: interrupt", "IR proximity, RGBC photodiodes and gesture engine", "short-range gesture, proximity and colour channels", "touchless switch, colour sorter demo", "₹450–950", "PAJ7620 / TCS34725", "https://www.broadcom.com/products/optical-sensors/gesture/apds-9960"),
("TCS34725 colour sensor", "tcs34725", "I²C", "2.7–3.3 V", "VIN: power; GND: return; SDA: data; SCL: clock; INT: interrupt; LED: illumination control (breakout)", "RGB-clear filtered photodiodes with ADC", "colour classification under controlled illumination", "colour sorter, LED calibration", "₹550–1,100", "APDS9960 / AS7341", "https://ams-osram.com/products/sensor-solutions/ambient-light-color-spectral-proximity-sensors/ams-tcs34725-color-sensor"),
("INA219 current / voltage", "ina219", "I²C", "3–5.5 V logic; bus ≤26 V", "VCC: power; GND: return; SDA: data; SCL: clock; VIN+: shunt high; VIN−: shunt load side", "High-side shunt voltage measurement with ADC", "bus voltage, current and power after calibration", "battery monitor, solar node, load profiling", "₹220–550", "INA226 / ACS712", "https://www.ti.com/product/INA219"),
("ACS712 current sensor", "acs712", "Analog voltage", "5 V", "VCC: 5 V; GND: return; OUT: analog current voltage; IP+/IP−: isolated-current path", "Hall-effect current measurement across integrated conductor", "AC/DC current waveform or level; calibrate zero offset", "motor current, overcurrent experiment", "₹180–450", "INA219 / SCT-013", "https://www.allegromicro.com/en/products/sense/current-sensor-ics/zero-to-fifty-amp-integrated-conductor-sensor-ics/acs712"),
("MAX6675 K-type thermocouple", "max6675", "SPI-like", "3.0–5.5 V", "VCC: power; GND: return; SCK: clock; CS: chip select; SO: data to MCU; T+/T−: thermocouple", "Cold-junction-compensated thermocouple-to-digital conversion", "high-temperature K-type measurement", "kiln monitor, exhaust experiment, reflow oven", "₹250–650", "MAX31855 / PT100 interface", "https://www.analog.com/en/products/max6675.html"),
("MLX90614 IR thermometer", "mlx90614", "I²C / SMBus", "3–5 V module", "VCC: power; GND: return; SDA: data; SCL: clock; PWM: optional output", "Thermopile measures emitted infrared radiation with ambient compensation", "non-contact surface temperature; emissivity matters", "touchless thermometer, hot-object alarm", "₹900–2,000", "thermal camera / DS18B20 contact", "https://www.melexis.com/en/product/mlx90614/datasheet"),
]

BOARDS = [
("Arduino Uno R3", "arduino-uno-r3", "ATmega328P, 16 MHz, 5 V", "14 digital I/O (6 PWM), 6 analog inputs", "USB-B: power/programming; D0/RX,D1/TX: UART; A4/SDA,A5/SCL: I²C; D10–13: SPI; 5V/3.3V/GND: rails", "₹700–1,800", "beginner 5 V prototyping", "Arduino Nano / ESP32", "https://docs.arduino.cc/hardware/uno-rev3/"),
("Arduino Nano", "arduino-nano", "ATmega328P, 16 MHz, 5 V", "14 digital I/O (6 PWM), 8 analog inputs", "Mini-B USB: programming; D0/D1: UART; A4/A5: I²C; D10–13: SPI; VIN/5V/3V3/GND: power", "₹350–1,200", "compact breadboard ATmega projects", "Uno / Pro Mini", "https://docs.arduino.cc/hardware/nano/"),
("Arduino Mega 2560", "arduino-mega-2560", "ATmega2560, 16 MHz, 5 V", "54 digital I/O (15 PWM), 16 analog inputs", "USB-B: programming; Serial0–3: UARTs; D20/SDA,D21/SCL: I²C; D50–53: SPI; VIN/5V/3.3V/GND: rails", "₹1,000–2,500", "many I/O and serial peripherals", "Uno / STM32", "https://docs.arduino.cc/hardware/mega-2560/"),
("ESP32 DevKit", "esp32-devkit", "ESP32 dual-core Wi‑Fi/BLE, 3.3 V", "GPIO varies; ADC, DAC (some), I²C, SPI, UART, PWM", "USB: power/programming; 3V3/GND: logic rail; GPIO21/22: common I²C; GPIO1/3: UART0; EN: reset; BOOT/GPIO0: flash mode", "₹350–900", "wireless IoT and higher processing", "ESP8266 / Raspberry Pi Pico W", "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/user-guide-devkitc.html"),
("ESP8266 NodeMCU", "esp8266-nodemcu", "ESP8266 Wi‑Fi, 3.3 V", "GPIO limited; one ADC; I²C/SPI/UART by pin mux", "Micro-USB: power/programming; 3V3/GND: logic; D1/D2: common I²C; TX/RX: UART; A0: ADC; EN/RST: control", "₹250–650", "low-cost Wi‑Fi sensor node", "ESP32 / Pico W", "https://arduino-esp8266.readthedocs.io/en/latest/boards.html"),
("Raspberry Pi Pico", "raspberry-pi-pico", "RP2040 dual-core, 3.3 V", "26 GPIO; ADC, UART, I²C, SPI, PWM, PIO", "Micro-USB: power/programming; VSYS: supply; 3V3_OUT: rail; GND: return; GP0/1: UART; GP4/5: I²C default; RUN: reset", "₹450–900", "fast deterministic I/O and MicroPython", "ESP32 / Arduino Nano", "https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html"),
("Raspberry Pi Pico W", "raspberry-pi-pico-w", "RP2040 + Wi‑Fi, 3.3 V", "26 GPIO; ADC, UART, I²C, SPI, PWM, PIO", "Micro-USB: power/programming; VSYS/3V3_OUT/GND: power; GPIO map matches Pico; wireless uses CYW43439", "₹650–1,200", "MicroPython wireless edge node", "ESP32 / Pico", "https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html"),
("STM32F103C8T6 Blue Pill", "stm32-blue-pill", "STM32F103C8T6 Cortex‑M3, 3.3 V", "GPIO with ADC, timers, I²C, SPI, UART, CAN", "3V3/GND: logic; PA9/PA10: UART1; PB6/PB7: I²C1 remap; PA5–7: SPI1; SWDIO/SWCLK: debug; BOOT0: boot select", "₹250–650", "low-cost ARM bare-metal learning", "Pico / Nucleo", "https://www.st.com/en/microcontrollers-microprocessors/stm32f103c8.html"),
("Arduino Pro Mini", "arduino-pro-mini", "ATmega328P, 3.3 V/8 MHz or 5 V/16 MHz", "14 digital I/O (6 PWM), 6 analog inputs", "FTDI: external programming UART; VCC: regulated rail; RAW: unregulated input; A4/A5: I²C; D10–13: SPI; GND: return", "₹250–600", "small low-power embedded deployment", "Nano / ATtiny", "https://docs.arduino.cc/retired/boards/arduino-pro-mini/"),
("Teensy 4.0", "teensy-4", "i.MX RT1062 Cortex‑M7, 600 MHz, 3.3 V", "many GPIO; ADC, I²C, SPI, UART, I²S, USB", "Micro-USB: programming/USB; VIN: 5 V input; 3.3V: rail; GND: return; pins support multiplexed serial/audio functions", "₹3,000–5,500", "high-performance audio/control", "ESP32-S3 / STM32", "https://www.pjrc.com/store/teensy40.html"),
]

def slugify(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def title(s): return s.replace('-', ' ').title()
def svg(path, name, interface, pins, kind):
    pinlist = [p.split(':')[0].strip() for p in pins.split(';')][:6]
    labels = ''.join(f'<text x="28" y="{105+i*29}" class="pin">{x}</text><circle cx="205" cy="{100+i*29}" r="5" class="dot"/>' for i,x in enumerate(pinlist))
    path.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="330" viewBox="0 0 760 330" role="img" aria-labelledby="t d"><title id="t">{name} reference pin illustration</title><desc id="d">Conceptual {kind} illustration listing common module pins.</desc><style>.bg{{fill:#081b2c}}.card{{fill:#12314a;stroke:#43d3b3;stroke-width:2}}.h{{font:700 25px sans-serif;fill:#fff}}.s{{font:15px sans-serif;fill:#b9d4e7}}.pin{{font:15px monospace;fill:#fff}}.dot{{fill:#ffca58}}</style><rect width="760" height="330" class="bg" rx="20"/><text x="28" y="42" class="h">{name}</text><text x="28" y="70" class="s">Conceptual pin reference • confirm the exact breakout silk screen</text><rect x="20" y="84" width="205" height="{max(185, 28*len(pinlist)+28)}" rx="13" class="card"/>{labels}<rect x="300" y="105" width="330" height="130" rx="20" class="card"/><text x="330" y="155" class="h">{kind.upper()}</text><text x="330" y="187" class="s">Interface: {interface}</text><path d="M630 170H710" stroke="#ffca58" stroke-width="5"/><path d="M700 160l15 10-15 10" fill="none" stroke="#ffca58" stroke-width="5"/></svg>''')

def sensor_doc(r):
    name, slug, iface, voltage, pins, technique, why, apps, price, compare, source = r
    recipe = ('analog-voltage' if 'Analog' in iface else 'i2c' if 'I²C' in iface else
              'spi' if 'SPI' in iface else 'single-wire-digital' if 'Single-wire' in iface else
              '1-wire' if '1-Wire' in iface else 'uart' if 'UART' in iface else
              'pulse-timing' if 'Pulse' in iface else 'digital-threshold' if 'Digital' in iface else
              'two-wire-synchronous' if 'Two-wire' in iface else 'i2s-digital-audio' if 'I²S' in iface else 'analog-voltage')
    pitems = '\n'.join(f'| `{a.strip()}` | {b.strip() or "See module documentation"} |' for x in pins.split(';') for a,b in [x.partition(':')[::2]])
    img=f'../../assets/illustrations/sensors/{slug}.svg'
    return f'''# {name}

![Conceptual {name} pin reference]({img})

> **Quick decision:** choose this for **{why}**. It communicates over **{iface}** and typical Indian retail pricing is **{price}** (indicative, checked catalogue range on {TODAY}; shipping, clones, probe and tax can change it).

## At a glance

| Property | Reference value |
|---|---|
| Common module interface | {iface} |
| Supply | {voltage} |
| Typical price in India | {price} |
| Same-job alternative | {compare} |
| Primary technique | {technique} |

## Pins — common breakout/module

> Pin order is **not universal**. Read the labels on the actual board and its datasheet before energising it.

| Pin | Use |
|---|---|
{pitems}

## How it works

{technique}. The module conditions or digitises that physical effect, then exposes it through {iface}. Treat raw readings as measurements requiring the stated calibration, warm-up, mounting and environmental controls.

```mermaid
flowchart LR
  P[Physical quantity] --> E[Sensor element]
  E --> C[Conditioning / ADC]
  C --> I[{iface}]
  I --> M[Microcontroller]
  M --> O[Serial log / control action]
```

## Where and why to use it

**Useful for:** {apps}. It is a practical choice when {why}; it is not a substitute for a safety-, medical-, or revenue-grade instrument unless the complete product is designed, calibrated and certified for that purpose.

## Two program paths, output and inference

Use the matching, complete sketches in the [program cookbook](../PROGRAM_COOKBOOK.md). They are intentionally small enough to adapt before integrating a library.

1. **Path A — interface bring-up:** use [the {iface} recipe](../PROGRAM_COOKBOOK.md#{recipe}). Confirm the bus/pulse/ADC data first.
2. **Path B — application loop:** use [the filtered alarm/logger recipe](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm). Replace `readSensor()` with the Path A acquisition and set thresholds only after calibration.

**Expected output:** a timestamped raw or converted reading in Serial Monitor; the alarm recipe reports `NORMAL` or `CHECK`.

**Inference:** a changing, plausible reading proves communication, **not accuracy**. Compare against a known reference, observe noise/range, and record offsets before making an automated decision.

## Comparison

| Choice | Prefer it when | Trade-off |
|---|---|---|
| **{name}** | {why} | Verify calibration, operating range and module variant |
| **{compare}** | you need a different accuracy, range, lifetime or interface | normally costs more or needs more integration |

## Advantages and limitations

**Advantages**
- Accessible module ecosystem and microcontroller support.
- Directly useful for {apps}.
- {iface} can be logged or acted on by a small controller.

**Limitations / precautions**
- Module pin labels, regulator and logic levels vary by seller; never assume 5 V tolerance.
- Results depend on placement, interference, warm-up and calibration.
- Do not use a hobby module alone for life safety, fire, gas safety, medical diagnosis or legal metering.

## Verification source

- Primary product/datasheet page: [{source.split('/')[2]}]({source})
- Catalogue policy, wiring conventions and price scope: [Reference policy](../REFERENCE_POLICY.md)
'''

def board_doc(r):
    name, slug, cpu, io, pins, price, why, compare, source = r
    pitems='\n'.join(f'| `{a.strip()}` | {b.strip() or "See board documentation"} |' for x in pins.split(';') for a,b in [x.partition(':')[::2]])
    return f'''# {name}

![Conceptual {name} board pin reference](../../assets/illustrations/boards/{slug}.svg)

> **Role:** {why}. Typical Indian retail range: **{price}** (indicative on {TODAY}, not a live quote).

| Property | Reference |
|---|---|
| Controller | {cpu} |
| I/O summary | {io} |
| Logic level | Check the board documentation; many pins are 3.3 V-only |
| Alternative | {compare} |

## Key pins and connectors

| Pin / connector | Use |
|---|---|
{pitems}

```mermaid
flowchart LR
  USB[USB / power] --> MCU[Microcontroller board]
  MCU --> GPIO[GPIO / ADC / PWM]
  MCU --> Buses[I²C · SPI · UART]
  Buses --> Sensors[Sensors & modules]
  GPIO --> Actuators[Drivers & actuators]
```

## Applications, technique and selection

The board executes firmware stored in its controller and uses digital/analog peripherals to sample sensors and drive outputs. Choose it for **{why}**: its processor, voltage domain, memory, connectivity and physical size determine whether it fits. Typical applications include data loggers, control panels, robotics and connected sensor nodes.

## Three first programs, output and inference

1. [Blink / GPIO smoke test](../PROGRAM_COOKBOOK.md#blink-gpio-smoke-test): LED changes every second — proves upload, clock and output pin.
2. [I²C scanner](../PROGRAM_COOKBOOK.md#i2c-scanner): serial output lists responding addresses — proves shared-bus wiring.
3. [Filtered telemetry and alarm](../PROGRAM_COOKBOOK.md#filtered-telemetry-and-alarm): serial readings and state — proves the acquisition-to-decision loop.

**Inference:** passing these tests does not establish voltage compatibility or sensor accuracy. Confirm common ground, logic levels, current budget and exact pin multiplexing before expansion.

## Comparison and trade-offs

| Board | Best when | Trade-off |
|---|---|---|
| **{name}** | {why} | Check its exact variant, USB interface and voltage limits |
| **{compare}** | requirements differ in wireless capability, speed, I/O or power | requires a different toolchain or wiring plan |

**Advantages:** popular tools/tutorials; flexible interfaces; fast iteration.

**Disadvantages:** development boards are not automatically rugged, low-power or electrically protected products; add regulator, protection, enclosure and driver circuitry where needed.

## Verification source

- Official documentation: [{source.split('/')[2]}]({source})
- [Reference policy](../REFERENCE_POLICY.md)
'''

def main():
    for d in ['docs/sensors','docs/boards','assets/illustrations/sensors','assets/illustrations/boards','examples']:
        (ROOT/d).mkdir(parents=True,exist_ok=True)
    for r in SENSORS:
        (ROOT/'docs/sensors'/f'{r[1]}.md').write_text(sensor_doc(r))
        svg(ROOT/'assets/illustrations/sensors'/f'{r[1]}.svg',r[0],r[2],r[4],'sensor')
    for r in BOARDS:
        (ROOT/'docs/boards'/f'{r[1]}.md').write_text(board_doc(r))
        svg(ROOT/'assets/illustrations/boards'/f'{r[1]}.svg',r[0],'GPIO / serial buses',r[4],'board')
    sensor_rows='\n'.join(f'| [{r[0]}](sensors/{r[1]}.md) | {r[2]} | {r[6]} | {r[8]} |' for r in SENSORS)
    board_rows='\n'.join(f'| [{r[0]}](boards/{r[1]}.md) | {r[1]} | {r[5]} | {r[6]} |' for r in BOARDS)
    (ROOT/'docs/SENSOR_CATALOG.md').write_text(f'''# Sensor catalogue

**{len(SENSORS)} documented sensors** · pin use · conceptual pin images · block diagrams · applications · INR range · techniques · comparisons · advantages/limits · two tested workflow paths per entry.

Prices are indicative Indian hobby-retail ranges on **{TODAY}**, not live listings. Read [Reference policy](REFERENCE_POLICY.md) before buying or wiring.

| Sensor | Interface | Choose it for | INR |
|---|---|---|---|
{sensor_rows}

## Browse by signal

- **Analog:** LM35, TMP36, NTC, MQ modules, LDR, distance IR, soil/rain/turbidity/TDS/pH, force/flex, microphone, INA/ACS and thermocouple interfaces.
- **I²C/SPI:** environmental, light, ToF, IMU, magnetometer, optical, current and IR-temperature devices.
- **Digital/timing:** DHT, DS18B20, ultrasonic, motion, reed/Hall and float switches.
- **UART:** particulate sensors and GPS.

For initial firmware and expected results, use the [Program cookbook](PROGRAM_COOKBOOK.md).
''')
    (ROOT/'docs/BOARD_CATALOG.md').write_text(f'''# Development-board catalogue

**{len(BOARDS)} documented boards** with pin roles, reference illustrations, architecture diagrams, price ranges, comparisons and bring-up programs.

| Board | Controller | INR | Choose it for |
|---|---|---|---|
{board_rows}

> Always use a common ground and check a board's logic voltage before connecting a module. A 5 V sensor output can damage a 3.3 V-only GPIO.
''')
    (ROOT/'docs/REFERENCE_POLICY.md').write_text(f'''# Reference and verification policy

## Scope

This library is a **starting reference**, not a wiring authority or a product certification. It was curated on **{TODAY}**. Each entry links the part maker or official board documentation where available. Clone modules often change regulators, pin order and tolerances.

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
''')
if __name__ == '__main__': main()
