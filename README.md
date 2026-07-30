# feign

Mock MicroPython libraries for CPython development and testing.

`feign` lets students write code that looks exactly like real MicroPython —
`import machine`, `import network`, and so on — while running and testing it on a
normal computer without any hardware attached.

## Quick start

Install with `uv`:

```bash
uv add --dev feign
```

Or with `pip`:

```bash
pip install feign
```

### Run a script with mocks

```bash
feign run main.py
# or
python -m feign main.py
```

If your script or an earlier import already loads `feign`, you can also use:

```bash
FEIGN=1 python main.py
```

### Run tests with mocks

`feign` registers a pytest plugin. Just run:

```bash
pytest
```

and `import machine` will work in your tests and the code they import.

> **Note:** under pytest, `feign` only installs MicroPython-specific module names
> such as `machine`, `network`, and `usocket`. It does **not** shadow CPython
> stdlib modules like `socket`, `time`, `os`, `json`, or `asyncio`, because those
> are needed by pytest and other tooling. Use `usocket`, `utime`, `uos`, `ujson`,
> and `uasyncio` in testable code, or run the code through `feign run` to get the
> non-`u` aliases as well.

### Override behavior for assignments

In `conftest.py` or test fixtures:

```python
import feign

feign.patch("machine.Pin.value", return_value=1)
feign.patch("network.WLAN.isconnected", return_value=True)
```

Or temporarily:

```python
with feign.override(machine_Pin_value=1):
    ...
```

### Create a new assignment

```bash
feign init my_assignment
```

This scaffolds a project with `pyproject.toml`, `conftest.py`, starter source,
tests, and `.pyi` stubs so editors know the mocked MicroPython APIs.

## Mocked modules

`feign` includes mocks for the full MicroPython standard library plus
common port-specific modules:

- `machine`, `network`, `bluetooth`, `framebuf`, `gc`, `micropython`
- `usocket` / `socket`, `utime` / `time`, `uos` / `os`, `usys` / `sys`
- `ujson` / `json`, `ubinascii` / `binascii`, `uhashlib` / `hashlib`
- `uerrno` / `errno`, `uheapq` / `heapq`, `uasyncio` / `asyncio`
- `uctypes` / `ctypes`, `ucollections` / `collections`, `ustruct` / `struct`
- `uselect` / `select`, `uzlib` / `zlib`
- `neopixel`, `dht`, `onewire`, `ds18x20`
- `esp`, `esp32`, `rp2`, `pyb`, `samd`, `zephyr`

## License

MIT
