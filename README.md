# mockro

Mock MicroPython libraries for CPython development and testing.

[![Documentation](https://img.shields.io/badge/docs-readthedocs-blue)](https://mockro.readthedocs.io/)

`mockro` lets developers write firmware code that uses real MicroPython APIs —
`import machine`, `import network`, and so on — and run it on a normal computer
without hardware attached. It is useful for local development, unit tests, CI,
and prototyping before deploying to a device.

Originally derived from educational workflows, `mockro` is packaged as a
standalone development and testing tool for embedded and IoT projects.

## Quick start

Install with `uv`:

```bash
uv add --dev mockro
```

Or with `pip`:

```bash
pip install mockro
```

### Run a script with mocks

Once `mockro` is installed in the environment, plain Python invocations work:

```bash
uv run python main.py
# or
python main.py
```

You can also use the explicit wrappers:

```bash
mockro run main.py
# or
python -m mockro main.py
```

### Run tests with mocks

`mockro` registers a pytest plugin. Just run:

```bash
pytest
```

and `import machine` will work in your tests and the code they import.

> **Note:** by default `mockro` only installs MicroPython-specific module names
> such as `machine`, `network`, and `usocket`. It does **not** shadow CPython
> stdlib modules like `socket`, `time`, `os`, `json`, or `asyncio`, because those
> are needed by pytest and other tooling. Use `usocket`, `utime`, `uos`, `ujson`,
> and `uasyncio` in testable code, or run the code through `mockro run` / `python -m mockro`
> to get the non-`u` aliases as well.

### Stub and override hardware behavior

In `conftest.py` or test fixtures:

```python
import mockro

mockro.patch("machine.Pin.value", return_value=1)
mockro.patch("network.WLAN.isconnected", return_value=True)
```

Or temporarily:

```python
with mockro.override(machine_Pin_value=1):
    ...
```

### Scaffold a new project

```bash
mockro init my_project
```

This creates a project with `pyproject.toml`, `conftest.py`, starter source,
tests, and `.pyi` stubs so editors know the mocked MicroPython APIs.

## Mocked modules

`mockro` includes mocks for the full MicroPython standard library plus
common port-specific modules:

- `machine`, `network`, `bluetooth`, `framebuf`, `gc`, `micropython`
- `usocket` / `socket`, `utime` / `time`, `uos` / `os`, `usys` / `sys`
- `ujson` / `json`, `ubinascii` / `binascii`, `uhashlib` / `hashlib`
- `uerrno` / `errno`, `uheapq` / `heapq`, `uasyncio` / `asyncio`
- `uctypes` / `ctypes`, `ucollections` / `collections`, `ustruct` / `struct`
- `uselect` / `select`, `uzlib` / `zlib`
- `neopixel`, `dht`, `onewire`, `ds18x20`
- `esp`, `esp32`, `rp2`, `pyb`, `samd`, `zephyr`

## Documentation

Full documentation is available at [mockro.readthedocs.io](https://mockro.readthedocs.io/).

## License

MIT
