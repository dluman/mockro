# Quick start

## Install

`mockro` requires Python 3.11 or later.

=== "uv"

    ```bash
    uv add --dev mockro
    ```

=== "pip"

    ```bash
    pip install mockro
    ```

## Run a script with mocks

Create a file named `main.py`:

```python title="main.py"
import machine
import network


def main() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)


if __name__ == "__main__":
    main()
```

Run it normally:

```bash
uv run python main.py
# or
python main.py
```

`mockro` installs itself via a `.pth` file, so MicroPython imports resolve to
mocks without any explicit activation.

## Run tests

`mockro` registers a pytest plugin. Write a test file and run `pytest`:

```python title="tests/test_led.py"
import machine


def test_led_turns_on() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()
    assert led.value() == 0  # default mock value
```

```bash
uv run pytest
```

## Override mock behavior

In `conftest.py` or a test fixture:

```python title="tests/conftest.py"
import mockro

mockro.patch("machine.Pin.value", return_value=1)
mockro.patch("network.WLAN.isconnected", return_value=True)
```

Now `led.value()` returns `1` and `wlan.isconnected()` returns `True`.

## Next steps

- Read the [usage guides](usage/testing.md) for more details.
- Browse the [examples](examples/led.md) for common patterns.
- Check the [API reference](reference/api.md) for the public API.
