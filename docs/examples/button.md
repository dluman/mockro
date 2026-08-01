# Button press

Testing a button usually means reading a digital input pin and reacting when it
goes high or low.

## Firmware code

```python title="src/button.py"
import machine


class Button:
    def __init__(self, pin: int) -> None:
        self._pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)

    def is_pressed(self) -> bool:
        # Active low: pressed means pin reads 0
        return self._pin.value() == 0
```

## Test released state

By default, `machine.Pin.value()` returns `0`, so the default mock would report
"pressed". Patch it to return `1` to represent the button being released:

```python title="tests/conftest.py"
import mockro

mockro.patch("machine.Pin.value", return_value=1)
```

```python title="tests/test_button.py"
from button import Button


def test_button_not_pressed_by_default() -> None:
    button = Button(0)
    assert not button.is_pressed()
```

## Test pressed state

Override the value for a single test:

```python title="tests/test_button.py"
import mockro
from button import Button


def test_button_pressed() -> None:
    with mockro.override(machine_Pin_value=0):
        button = Button(0)
        assert button.is_pressed()
```

## Test a sequence of presses

```python title="tests/test_button.py"
import mockro
from button import Button


def test_button_bounce() -> None:
    mockro.patch("machine.Pin.value", side_effect=[1, 1, 0, 0, 1, 0, 1])
    button = Button(0)

    states = [button.is_pressed() for _ in range(7)]
    assert states == [False, False, True, True, False, True, False]
```

## Verify the pin was configured

Use the recorder to assert the pin was created with the expected arguments:

```python title="tests/test_button.py"
import mockro
from button import Button


def test_button_pin_configuration() -> None:
    button = Button(0)
    init_calls = mockro.get_recorder().calls("machine.Pin.__init__")
    assert len(init_calls) == 1

    args, kwargs = init_calls[0]
    pin_id, mode, pull = args[1], args[2], args[3]
    assert pin_id == 0
    assert mode == mockro.get_recorder().calls("machine.Pin.IN")  # see below
```

!!! note

    `machine.Pin.IN` and `machine.Pin.PULL_UP` are constants; they are not
    recorded as calls. Access them directly for assertions:
    `machine.Pin.IN == 0` and `machine.Pin.PULL_UP == 4`.
