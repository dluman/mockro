# Module aliases

MicroPython provides two naming conventions for many standard-library modules:

- The `u` prefix: `usocket`, `utime`, `uos`, `ujson`, `uasyncio`, ...
- The bare name: `socket`, `time`, `os`, `json`, `asyncio`, ...

`mockro` supports both, but the two conventions are treated differently so
that `pytest` and other CPython tooling keep working.

## `u` names (always available)

MicroPython-specific names with the `u` prefix are safe to install globally
because they do not shadow CPython stdlib modules. `mockro` makes these
available whenever it is installed:

- `usocket`, `utime`, `uos`, `usys`
- `ujson`, `ubinascii`, `uhashlib`, `uerrno`
- `uheapq`, `uasyncio`, `uctypes`, `ucollections`, `ustruct`
- `uselect`, `uzlib`

Write testable code with these names:

```python
import utime

utime.sleep_ms(100)
```

## Bare names (available on request)

The bare names shadow CPython stdlib modules. `mockro` only installs them when
explicitly requested, so `pytest`, `asyncio`, `json`, and other tools continue to
use the real CPython implementations.

Activate the bare aliases with:

```python
import mockro

mockro.activate(aliases=True)

import socket
```

Or run the script through the CLI:

```bash
mockro run main.py
```

## Why this matters

`pytest` and many CPython tools rely on `socket`, `time`, `os`, `json`, and
`asyncio`. If `mockro` replaced those globally, the test runner would break.
By defaulting to the `u` names, `mockro` stays compatible with the CPython
tooling ecosystem while still supporting your firmware code.

## Reference table

| MicroPython | `u` name | bare name | notes |
|-------------|----------|-----------|-------|
| socket | `usocket` | `socket` | bare alias needs `aliases=True` |
| time | `utime` | `time` | bare alias needs `aliases=True` |
| os | `uos` | `os` | bare alias needs `aliases=True` |
| sys | `usys` | `sys` | bare alias needs `aliases=True` |
| json | `ujson` | `json` | bare alias needs `aliases=True` |
| binascii | `ubinascii` | `binascii` | bare alias needs `aliases=True` |
| hashlib | `uhashlib` | `hashlib` | bare alias needs `aliases=True` |
| errno | `uerrno` | `errno` | bare alias needs `aliases=True` |
| heapq | `uheapq` | `heapq` | bare alias needs `aliases=True` |
| asyncio | `uasyncio` | `asyncio` | bare alias needs `aliases=True` |
| ctypes | `uctypes` | `ctypes` | bare alias needs `aliases=True` |
| collections | `ucollections` | `collections` | bare alias needs `aliases=True` |
| struct | `ustruct` | `struct` | bare alias needs `aliases=True` |
| select | `uselect` | `select` | bare alias needs `aliases=True` |
| zlib | `uzlib` | `zlib` | bare alias needs `aliases=True` |
| gc | `gc` | `gc` | bare alias needs `aliases=True` |

All other mocked modules (`machine`, `network`, `bluetooth`, `framebuf`, etc.)
are always available.
