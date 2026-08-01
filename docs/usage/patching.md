# Patching and overriding

`mockro` lets you replace the behavior of mocked functions, methods, or classes.
This is how tests simulate hardware state without a real device.

## `mockro.patch`

`patch` takes a dotted target name and a replacement value, callable, or
return value.

```python
import mockro

mockro.patch("machine.Pin.value", return_value=1)
```

### Use a callable

```python
import mockro

def read_sensor():
    return 42

mockro.patch("machine.ADC.read", obj=read_sensor)
```

### Use a side effect

A side effect can be an iterable, where each call returns the next value:

```python
import mockro

mockro.patch("machine.Pin.value", side_effect=[0, 1, 0, 1])
```

Or a callable that runs arbitrary logic:

```python
import mockro

def raise_when_closed(*args, **kwargs):
    raise RuntimeError("door closed")

mockro.patch("machine.Pin.value", side_effect=raise_when_closed)
```

## `mockro.override`

`override` is a context manager for temporary patches. Keyword names use
underscores instead of dots:

```python
import mockro
import machine


def test_led_blink() -> None:
    led = machine.Pin(2, machine.Pin.OUT)

    with mockro.override(machine_Pin_value=1):
        assert led.value() == 1

    assert led.value() == 0
```

You can override multiple targets at once:

```python
with mockro.override(machine_Pin_value=1, network_WLAN_isconnected=True):
    ...
```

## Class-level overrides

You can replace an entire class with a custom object:

```python
import mockro
import machine


class CustomPin:
    def __init__(self, *args, **kwargs):
        pass

    def value(self) -> int:
        return 42


mockro.patch("machine.Pin", CustomPin)
pin = machine.Pin(2)
assert pin.value() == 42
```

## Creating new mocks

For library authors, `mockro.mock_function` and `mockro.mock_class` create
new mocks that hook into the registry and recorder:

```python
from mockro import mock_function

read_temp = mock_function("mylib.read_temp", default_return=20.0)
```

See the [API reference](../reference/api.md) for full signatures.
