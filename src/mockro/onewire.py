"""Mock implementation of the MicroPython ``onewire`` module."""

from __future__ import annotations

from typing import Any

from mockro._factory import mock_class, mock_function


@mock_class("onewire.OneWire")
class OneWire:
    """Mock 1-Wire bus controller."""

    _init = mock_function("onewire.OneWire.__init__", default_return=None)
    _reset = mock_function("onewire.OneWire.reset", default_return=True)
    _readbit = mock_function("onewire.OneWire.readbit", default_return=0)
    _readbyte = mock_function("onewire.OneWire.readbyte", default_return=0)
    _readinto = mock_function("onewire.OneWire.readinto", default_return=None)
    _writebit = mock_function("onewire.OneWire.writebit", default_return=None)
    _writebyte = mock_function("onewire.OneWire.writebyte", default_return=None)
    _write = mock_function("onewire.OneWire.write", default_return=None)
    _select_rom = mock_function("onewire.OneWire.select_rom", default_return=None)
    _scan = mock_function("onewire.OneWire.scan", default_return=list)
    _crc8 = mock_function("onewire.OneWire.crc8", default_return=0)

    MATCH_ROM = 0x55
    SKIP_ROM = 0xCC
    SEARCH_ROM = 0xF0

    def __init__(self, pin: Any) -> None:
        self._init(self, pin)

    def reset(self, required: bool = False) -> bool:
        return self._reset(self, required)

    def readbit(self) -> int:
        return self._readbit(self)

    def readbyte(self) -> int:
        return self._readbyte(self)

    def readinto(self, buf: bytearray) -> None:
        self._readinto(self, buf)

    def writebit(self, value: int) -> None:
        self._writebit(self, value)

    def writebyte(self, value: int) -> None:
        self._writebyte(self, value)

    def write(self, buf: bytes) -> None:
        self._write(self, buf)

    def select_rom(self, rom: bytes) -> None:
        self._select_rom(self, rom)

    def scan(self) -> list[Any]:
        return self._scan(self)

    def crc8(self, data: bytes) -> int:
        return self._crc8(self, data)


@mock_class("onewire.OneWireError")
class OneWireError(Exception):
    """Mock 1-Wire error."""
