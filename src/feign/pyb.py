"""Mock implementation of the Pyboard-specific ``pyb`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function


@mock_class("pyb.LED")
class LED:
    """Mock Pyboard LED."""

    _init = mock_function("pyb.LED.__init__", default_return=None)
    _on = mock_function("pyb.LED.on", default_return=None)
    _off = mock_function("pyb.LED.off", default_return=None)
    _toggle = mock_function("pyb.LED.toggle", default_return=None)
    _intensity = mock_function("pyb.LED.intensity", default_return=0)

    def __init__(self, id: int) -> None:
        self._init(self, id)

    def on(self) -> None:
        self._on(self)

    def off(self) -> None:
        self._off(self)

    def toggle(self) -> None:
        self._toggle(self)

    def intensity(self, value: Any = None) -> Any:
        return self._intensity(self, value)


@mock_class("pyb.Switch")
class Switch:
    """Mock Pyboard switch."""

    _init = mock_function("pyb.Switch.__init__", default_return=None)
    _value = mock_function("pyb.Switch.value", default_return=False)
    _callback = mock_function("pyb.Switch.callback", default_return=None)

    def __init__(self) -> None:
        self._init(self)

    def value(self) -> bool:
        return self._value(self)

    def callback(self, func: Any = None) -> Any:
        return self._callback(self, func)


@mock_class("pyb.Accel")
class Accel:
    """Mock Pyboard accelerometer."""

    _init = mock_function("pyb.Accel.__init__", default_return=None)
    _x = mock_function("pyb.Accel.x", default_return=0)
    _y = mock_function("pyb.Accel.y", default_return=0)
    _z = mock_function("pyb.Accel.z", default_return=0)
    _tilt = mock_function("pyb.Accel.tilt", default_return=0)
    _filtered_xyz = mock_function("pyb.Accel.filtered_xyz", default_return=lambda: (0, 0, 0))

    def __init__(self) -> None:
        self._init(self)

    def x(self) -> int:
        return self._x(self)

    def y(self) -> int:
        return self._y(self)

    def z(self) -> int:
        return self._z(self)

    def tilt(self) -> int:
        return self._tilt(self)

    def filtered_xyz(self) -> tuple[Any, ...]:
        return self._filtered_xyz(self)


@mock_class("pyb.Servo")
class Servo:
    """Mock Pyboard servo controller."""

    _init = mock_function("pyb.Servo.__init__", default_return=None)
    _angle = mock_function("pyb.Servo.angle", default_return=0)
    _speed = mock_function("pyb.Servo.speed", default_return=0)
    _pulse_width = mock_function("pyb.Servo.pulse_width", default_return=1500)
    _calibration = mock_function("pyb.Servo.calibration", default_return=None)

    def __init__(self, id: int) -> None:
        self._init(self, id)

    def angle(self, value: Any = None) -> Any:
        return self._angle(self, value)

    def speed(self, value: Any = None) -> Any:
        return self._speed(self, value)

    def pulse_width(self, value: Any = None) -> Any:
        return self._pulse_width(self, value)

    def calibration(self, *args: Any) -> Any:
        return self._calibration(self, *args)


delay = mock_function("pyb.delay", default_return=lambda ms: None)
udelay = mock_function("pyb.udelay", default_return=lambda us: None)
millis = mock_function("pyb.millis", default_return=0)
micros = mock_function("pyb.micros", default_return=0)
elapsed_millis = mock_function("pyb.elapsed_millis", default_return=lambda start: 0)
elapsed_micros = mock_function("pyb.elapsed_micros", default_return=lambda start: 0)
hard_reset = mock_function("pyb.hard_reset", default_return=None)
info = mock_function("pyb.info", default_return=None)
unique_id = mock_function("pyb.unique_id", default_return=lambda: b"\x00" * 12)
freq = mock_function("pyb.freq", default_return=lambda: (168_000_000, 24_000_000, 42_000_000))
repl_uart = mock_function("pyb.repl_uart", default_return=None)
usb_mode = mock_function("pyb.usb_mode", default_return=None)
have_cdc = mock_function("pyb.have_cdc", default_return=True)
hid = mock_function("pyb.hid", default_return=None)
main = mock_function("pyb.main", default_return=None)
mount = mock_function("pyb.mount", default_return=None)
