# LED blink

A common first embedded program is blinking an LED. With `mockro`, you can test
that logic without a real board.

## Firmware code

```python title="src/main.py"
import machine
import utime


class LED:
    def __init__(self, pin: int) -> None:
        self._pin = machine.Pin(pin, machine.Pin.OUT)

    def on(self) -> None:
        self._pin.on()

    def off(self) -> None:
        self._pin.off()

    def blink(self, times: int, delay_ms: int) -> None:
        for _ in range(times):
            self.on()
            utime.sleep_ms(delay_ms)
            self.off()
            utime.sleep_ms(delay_ms)


def main() -> None:
    led = LED(2)
    led.blink(3, 500)


if __name__ == "__main__":
    main()
```

## Test with default mocks

```python title="tests/test_led.py"
import machine
from main import LED


def test_led_starts_off() -> None:
    led = LED(2)
    assert led._pin.value() == 0
```

## Test with overrides

Make the pin read back as `1` when it is on:

```python title="tests/conftest.py"
import mockro

mockro.patch("machine.Pin.value", return_value=1)
```

```python title="tests/test_led.py"
from main import LED


def test_led_on_value() -> None:
    led = LED(2)
    led.on()
    assert led._pin.value() == 1
```

## Test with side effects

Simulate a blink sequence:

```python title="tests/test_led.py"
import mockro
from main import LED


def test_blink_sequence() -> None:
    mockro.patch("machine.Pin.value", side_effect=[0, 1, 0, 1, 0])
    led = LED(2)
    led.blink(2, 10)

    value_calls = mockro.get_recorder().calls("machine.Pin.value")
    assert len(value_calls) == 5
```

!!! tip

    The exact call count depends on how your `LED` class queries the pin. Use
    `get_recorder().calls()` to inspect the recorded arguments.
