"""Mock implementation of the MicroPython ``uctypes`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function

INT8 = 1
INT16 = 2
INT32 = 3
INT64 = 4
UINT8 = 5
UINT16 = 6
UINT32 = 7
UINT64 = 8
FLOAT32 = 9
FLOAT64 = 10
VOID = 11
PTR = 12
ARRAY = 13
LITTLE_ENDIAN = 0
BIG_ENDIAN = 1
NATIVE = 2

sizeof = mock_function("uctypes.sizeof", default_return=0)
addressof = mock_function("uctypes.addressof", default_return=0)
bytes_at = mock_function("uctypes.bytes_at", default_return=lambda addr, size: b"\x00" * size)
bytearray_at = mock_function(
    "uctypes.bytearray_at", default_return=lambda addr, size: bytearray(size)
)


@mock_class("uctypes.struct")
class struct:
    """Mock ctypes struct proxy."""

    _init = mock_function("uctypes.struct.__init__", default_return=None)

    def __init__(self, addr: int, descriptor: Any, layout_type: int = NATIVE) -> None:
        self._init(self, addr, descriptor, layout_type)


@mock_class("uctypes.union")
class union(struct):
    """Mock ctypes union proxy."""


@mock_class("uctypes.bytearray")
class bytearray_:
    """Mock ctypes bytearray proxy."""

    _init = mock_function("uctypes.bytearray.__init__", default_return=None)

    def __init__(self, data: Any) -> None:
        self._init(self, data)
