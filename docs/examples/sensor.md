# I2C sensor

Many sensors expose an I2C interface. `mockro`'s `machine.I2C` mock lets you
develop and test the driver code without wiring up hardware.

## Firmware code

```python title="src/bmp280.py"
import machine


class BMP280:
    ADDRESS = 0x76

    def __init__(self, i2c: machine.I2C) -> None:
        self._i2c = i2c

    def read_id(self) -> int:
        data = self._i2c.readfrom_mem(self.ADDRESS, 0xD0, 1)
        return data[0]

    def read_temperature(self) -> float:
        data = self._i2c.readfrom_mem(self.ADDRESS, 0xFA, 3)
        raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        # Simplified: real driver would apply calibration
        return raw / 100.0
```

## Test reading the chip ID

```python title="tests/test_bmp280.py"
import mockro
from bmp280 import BMP280


class FakeI2C:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8):
        if memaddr == 0xD0:
            return b"\x58"  # BMP280 chip ID
        return b"\x00" * nbytes


mockro.patch("machine.I2C", FakeI2C)


def test_read_chip_id() -> None:
    sensor = BMP280(machine.I2C(0))
    assert sensor.read_id() == 0x58
```

## Test temperature conversion

```python title="tests/test_bmp280.py"
import mockro
from bmp280 import BMP280


def test_read_temperature() -> None:
    class FakeI2C:
        def __init__(self, *args, **kwargs) -> None:
            pass

        def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8):
            # raw = 0x12345 -> 74565 -> 745.65
            return b"\x01\x23\x45"

    mockro.patch("machine.I2C", FakeI2C)
    sensor = BMP280(machine.I2C(0))

    assert sensor.read_temperature() == 745.65
```

## Test with the recorder

If the driver only needs to verify the right register was read, use the default
mock and assert calls:

```python title="tests/test_bmp280.py"
import mockro
from bmp280 import BMP280


def test_read_id_calls_correct_register() -> None:
    sensor = BMP280(machine.I2C(0))
    sensor.read_id()

    calls = mockro.get_recorder().calls("machine.I2C.readfrom_mem")
    assert len(calls) == 1

    addr, memaddr, nbytes = calls[0][0][1], calls[0][0][2], calls[0][0][3]
    assert addr == 0x76
    assert memaddr == 0xD0
    assert nbytes == 1
```

!!! tip

    For simple drivers, class-level overrides are often cleaner than patching
    individual methods. Replace `machine.I2C` with a small fake class that
    returns canned responses.
