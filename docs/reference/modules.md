# Mocked modules

`mockro` provides mocks for the full MicroPython standard library plus common
port-specific modules.

## MicroPython standard library

- `machine` — GPIO, timers, UART, I2C, SPI, ADC, PWM, RTC, WDT, and more.
- `network` — Wi-Fi and network interface management.
- `bluetooth` — BLE stack.
- `framebuf` — Frame buffer utilities.
- `gc` — Garbage collector.
- `micropython` — MicroPython-specific functions.

## `u` names and aliases

MicroPython-specific names that do not shadow CPython stdlib modules:

- `usocket` / `socket`
- `utime` / `time`
- `uos` / `os`
- `usys` / `sys`
- `ujson` / `json`
- `ubinascii` / `binascii`
- `uhashlib` / `hashlib`
- `uerrno` / `errno`
- `uheapq` / `heapq`
- `uasyncio` / `asyncio`
- `uctypes` / `ctypes`
- `ucollections` / `collections`
- `ustruct` / `struct`
- `uselect` / `select`
- `uzlib` / `zlib`

See [Module aliases](../usage/aliases.md) for the difference between `u` and
bare names.

## Hardware driver modules

- `neopixel` — WS2812 LEDs
- `dht` — DHT temperature/humidity sensors
- `onewire` — 1-Wire bus
- `ds18x20` — DS18B20 temperature sensors

## Port-specific modules

- `esp` — ESP8266/ESP32 generic
- `esp32` — ESP32-specific
- `rp2` — Raspberry Pi Pico (RP2040)
- `pyb` — Pyboard
- `samd` — Microchip SAMD
- `zephyr` — Zephyr port

## Notes

- Most mocks return safe defaults such as `0`, `None`, `False`, or empty
  collections.
- Methods and classes support the same override and recording machinery as the
  rest of `mockro`.
- If a module you need is missing, you can create a custom mock with
  `mockro.mock_function` and `mockro.mock_class`.
