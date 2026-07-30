"""Mock implementation of the MicroPython ``ds18x20`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function


@mock_class("ds18x20.DS18X20")
class DS18X20:
    """Mock DS18B20 / DS18S20 temperature sensor driver."""

    _init = mock_function("ds18x20.DS18X20.__init__", default_return=None)
    _scan = mock_function("ds18x20.DS18X20.scan", default_return=list)
    _convert_temp = mock_function("ds18x20.DS18X20.convert_temp", default_return=None)
    _read_scratch = mock_function(
        "ds18x20.DS18X20.read_scratch",
        default_return=lambda self, rom: b"\x00\x00\x00\x00\x00\x00\x00\x00\x00",
    )
    _write_scratch = mock_function("ds18x20.DS18X20.write_scratch", default_return=None)
    _read_temp = mock_function("ds18x20.DS18X20.read_temp", default_return=22.0)

    def __init__(self, onewire: Any) -> None:
        self._init(self, onewire)

    def scan(self) -> list[Any]:
        return self._scan(self)

    def convert_temp(self) -> None:
        self._convert_temp(self)

    def read_scratch(self, rom: bytes) -> bytes:
        return self._read_scratch(self, rom)

    def write_scratch(self, rom: bytes, data: bytes) -> None:
        self._write_scratch(self, rom, data)

    def read_temp(self, rom: bytes) -> float:
        return self._read_temp(self, rom)


def __getattr__(name: str) -> Any:
    if name == "DS18B20":
        return DS18X20
    if name == "DS18S20":
        return DS18X20
    raise AttributeError(f"module 'ds18x20' has no attribute '{name}'")
