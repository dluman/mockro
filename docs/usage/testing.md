# Testing with pytest

`mockro` registers a pytest plugin that activates mocks before tests are
collected and cleans up after each test.

## What the plugin does

- Installs the mock MicroPython modules before test collection.
- Takes a snapshot of the override registry before each test.
- Restores the snapshot and clears the recorder after each test.

This means patches made in `conftest.py` or session-scoped fixtures stay in
place, but local patches from one test do not leak into the next.

## Writing tests

Tests look like normal Python tests. Import MicroPython modules directly:

```python title="tests/test_led.py"
import machine


def test_led_default_value() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    assert led.value() == 0
```

Run tests as usual:

```bash
uv run pytest
```

## Global overrides in `conftest.py`

For behavior that should apply to every test, add patches to `conftest.py`:

```python title="tests/conftest.py"
import mockro

mockro.patch("machine.Pin.value", return_value=1)
mockro.patch("network.WLAN.isconnected", return_value=True)
```

## Local overrides with fixtures

Use a fixture when you want to vary behavior per test:

```python title="tests/conftest.py"
import pytest
import mockro


@pytest.fixture
def button_pressed():
    mockro.patch("machine.Pin.value", return_value=1)
```

```python title="tests/test_button.py"
import machine


def test_button_pressed(button_pressed) -> None:
    button = machine.Pin(0, machine.Pin.IN)
    assert button.value() == 1
```

## Temporary overrides

Use `mockro.override()` for a context manager that reverts automatically:

```python
import mockro
import machine


def test_led_on_only_inside_context() -> None:
    led = machine.Pin(2, machine.Pin.OUT)

    with mockro.override(machine_Pin_value=1):
        assert led.value() == 1

    assert led.value() == 0
```

See [Patching and overriding](patching.md) for more override options.
