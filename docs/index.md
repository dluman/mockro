# mockro

Mock MicroPython libraries for CPython development and testing.

`mockro` lets developers write firmware code that uses real MicroPython APIs —
`import machine`, `import network`, and so on — and run it on a normal computer
without hardware attached. It is useful for local development, unit tests, CI,
and prototyping before deploying to a device.

Originally derived from educational workflows, `mockro` is packaged as a
standalone development and testing tool for embedded and IoT projects.

## What it does

- Provides drop-in mocks for MicroPython modules such as `machine`, `network`,
  `usocket`, `utime`, and many more.
- Installs itself automatically when you use `pytest`.
- Lets you override mock behavior in tests or scripts.
- Records calls to mocked hardware so you can assert interactions.

## Where to start

- **[Quick start](quickstart.md)** — install, run a script, and run tests.
- **[Usage guides](usage/testing.md)** — detailed guides for running, testing,
  patching, and recording.
- **[Examples](examples/led.md)** — common patterns for LEDs, buttons, Wi-Fi,
  sensors, and project scaffolding.
- **[API reference](reference/api.md)** — public `mockro` API documentation.
