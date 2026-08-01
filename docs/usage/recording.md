# Recording calls

When a mocked function or method has no override, `mockro` records each call.
This lets tests assert that firmware interacted with hardware in the expected
way, even when the default return value is not important.

## The recorder

The recorder is a process-wide singleton. Access it with `mockro.get_recorder()`:

```python
import mockro

recorder = mockro.get_recorder()
```

## Recording calls

Calls are recorded automatically when there is no override:

```python
import mockro
import machine


def test_led_was_read() -> None:
    mockro.get_recorder().clear()
    mockro.activate()

    led = machine.Pin(2, machine.Pin.OUT)
    led.value()
    led.on()

    calls = mockro.get_recorder().calls("machine.Pin.value")
    assert len(calls) == 1
```

!!! note

    The pytest plugin clears the recorder automatically after each test, so you
    rarely need to call `clear()` in tests.

## Inspecting call arguments

`calls(name)` returns a list of `(args, kwargs)` tuples:

```python
calls = mockro.get_recorder().calls("machine.Pin.__init__")
args, kwargs = calls[0]

assert args[1] == 2  # pin id
assert kwargs == {}
```

## Example: assert a UART was configured

```python
import machine


def test_uart_configured() -> None:
    uart = machine.UART(1, baudrate=9600)
    uart.write(b"hello")

    init_calls = mockro.get_recorder().calls("machine.UART.__init__")
    assert len(init_calls) == 1

    write_calls = mockro.get_recorder().calls("machine.UART.write")
    assert len(write_calls) == 1
    assert write_calls[0][0][1] == b"hello"
```
