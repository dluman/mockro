"""Mock implementation of the ESP32-specific ``esp32`` module."""

from __future__ import annotations

from typing import Any

from mockro._factory import mock_class, mock_function

wake_on_touch = mock_function("esp32.wake_on_touch", default_return=None)
wake_on_ext0 = mock_function("esp32.wake_on_ext0", default_return=None)
wake_on_ext1 = mock_function("esp32.wake_on_ext1", default_return=None)
gpio_deep_sleep_hold = mock_function("esp32.gpio_deep_sleep_hold", default_return=None)


@mock_class("esp32.ULP")
class ULP:
    """Mock ESP32 ultra-low-power coprocessor."""

    _init = mock_function("esp32.ULP.__init__", default_return=None)
    _set_wakeup_period = mock_function("esp32.ULP.set_wakeup_period", default_return=None)
    _load_binary = mock_function("esp32.ULP.load_binary", default_return=None)
    _run = mock_function("esp32.ULP.run", default_return=None)

    def __init__(self) -> None:
        self._init(self)

    def set_wakeup_period(self, period_index: int, period_us: int) -> None:
        self._set_wakeup_period(self, period_index, period_us)

    def load_binary(self, load_addr: int, program: bytes) -> None:
        self._load_binary(self, load_addr, program)

    def run(self, entry_point: int) -> None:
        self._run(self, entry_point)


@mock_class("esp32.NVS")
class NVS:
    """Mock ESP32 non-volatile storage."""

    _init = mock_function("esp32.NVS.__init__", default_return=None)
    _get_i32 = mock_function("esp32.NVS.get_i32", default_return=0)
    _set_i32 = mock_function("esp32.NVS.set_i32", default_return=None)
    _commit = mock_function("esp32.NVS.commit", default_return=None)
    _erase_key = mock_function("esp32.NVS.erase_key", default_return=None)

    def __init__(self, name: str) -> None:
        self._init(self, name)

    def get_i32(self, key: str) -> int:
        return self._get_i32(self, key)

    def set_i32(self, key: str, value: int) -> None:
        self._set_i32(self, key, value)

    def commit(self) -> None:
        self._commit(self)

    def erase_key(self, key: str) -> None:
        self._erase_key(self, key)


@mock_class("esp32.Partition")
class Partition:
    """Mock ESP32 flash partition."""

    _init = mock_function("esp32.Partition.__init__", default_return=None)
    _find = mock_function("esp32.Partition.find", default_return=list)
    _info = mock_function(
        "esp32.Partition.info", default_return=lambda: (0, "mock", 0, 0, "mock", 0)
    )
    _readblocks = mock_function("esp32.Partition.readblocks", default_return=0)
    _writeblocks = mock_function("esp32.Partition.writeblocks", default_return=0)
    _ioctl = mock_function("esp32.Partition.ioctl", default_return=0)
    _set_boot = mock_function("esp32.Partition.set_boot", default_return=None)
    _get_next_update = mock_function("esp32.Partition.get_next_update", default_return=None)

    RUNNING = 0
    BOOT = 1
    TYPE_APP = 0
    TYPE_DATA = 1

    def __init__(self, id: Any, block_size: int = 0, offset: int = 0) -> None:
        self._init(self, id, block_size, offset)

    @classmethod
    def find(cls, type: int = 0, subtype: int = 0, label: str | None = None) -> list[Any]:
        return cls._find(type, subtype, label)

    def info(self) -> tuple[Any, ...]:
        return self._info(self)

    def readblocks(self, block_num: int, buf: bytearray) -> int:
        return self._readblocks(self, block_num, buf)

    def writeblocks(self, block_num: int, buf: bytes) -> int:
        return self._writeblocks(self, block_num, buf)

    def ioctl(self, op: int, arg: Any) -> int:
        return self._ioctl(self, op, arg)

    def set_boot(self) -> None:
        self._set_boot(self)

    def get_next_update(self) -> Partition:
        return self._get_next_update(self)


@mock_class("esp32.RMT")
class RMT:
    """Mock ESP32 remote control peripheral."""

    _init = mock_function("esp32.RMT.__init__", default_return=None)
    _source_freq = mock_function("esp32.RMT.source_freq", default_return=80_000_000)
    _clock_div = mock_function("esp32.RMT.clock_div", default_return=8)
    _wait_done = mock_function("esp32.RMT.wait_done", default_return=None)
    _loop = mock_function("esp32.RMT.loop", default_return=None)
    _write_pulses = mock_function("esp32.RMT.write_pulses", default_return=None)

    def __init__(
        self,
        channel: int,
        *,
        pin: Any = None,
        clock_div: int = 8,
        carrier_freq: int = 0,
        carrier_duty_percent: int = 50,
    ) -> None:
        self._init(
            self,
            channel,
            pin=pin,
            clock_div=clock_div,
            carrier_freq=carrier_freq,
            carrier_duty_percent=carrier_duty_percent,
        )

    def source_freq(self) -> int:
        return self._source_freq(self)

    def clock_div(self) -> int:
        return self._clock_div(self)

    def wait_done(self, timeout: int = 0) -> None:
        self._wait_done(self, timeout)

    def loop(self, enable_loop: bool) -> None:
        self._loop(self, enable_loop)

    def write_pulses(self, duration: Any, start: int = 1) -> None:
        self._write_pulses(self, duration, start)


IDF = mock_function("esp32.idf_heap_info", default_return=lambda: [])
raw_temperature = mock_function("esp32.raw_temperature", default_return=25.0)
hall_sensor = mock_function("esp32.hall_sensor", default_return=0)


def __getattr__(name: str) -> Any:
    if name in ("WAKEUP_ALL_LOW", "WAKEUP_ANY_HIGH"):
        return 0
    raise AttributeError(f"module 'esp32' has no attribute '{name}'")
