# Running scripts

`mockro` makes MicroPython imports work in ordinary CPython scripts. There are
a few ways to activate the mocks depending on how isolated the script needs to be.

## Automatic activation (recommended for development)

When `mockro` is installed, it registers a `.pth` file that activates the
MicroPython-specific module mocks automatically. This means the following
just works:

```bash
python main.py
uv run python main.py
```

Only module names that do not conflict with CPython stdlib modules are
installed this way — for example, `machine`, `network`, `usocket`, and `utime`.

## Explicit activation via `mockro activate`

For programs or test harnesses that need to control exactly when mocks are
available, call `mockro.activate()`:

```python
import mockro

mockro.activate()

import machine

pin = machine.Pin(2, machine.Pin.OUT)
```

By default, `activate()` only installs safe MicroPython-specific names. Pass
`aliases=True` to also install the non-`u` aliases such as `socket`, `time`,
`os`, and `json`:

```python
mockro.activate(aliases=True)

import socket  # resolves to mockro's socket mock
```

## Running with the `mockro` CLI

The `mockro run` command activates mocks in a fresh subprocess:

```bash
mockro run main.py
# or
python -m mockro run main.py
```

This is equivalent to calling `mockro.activate(aliases=True)` before executing
the script, so non-`u` aliases are available.

## When to use each approach

| Approach | Aliases available | Best for |
|----------|-------------------|----------|
| `python main.py` | `u*` names only | Day-to-day development, pytest |
| `mockro.activate()` | configurable | Libraries, notebooks, test harnesses |
| `mockro run main.py` | all | Scripts that use `socket`, `time`, `os`, etc. |

See [Module aliases](aliases.md) for the full list of `u*` and non-`u` names.
