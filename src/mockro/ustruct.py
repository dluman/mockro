"""Mock implementation of the MicroPython ``ustruct`` module."""

from __future__ import annotations

import struct as _struct
from typing import Any

from mockro._factory import mock_function

pack = mock_function("ustruct.pack", default_return=_struct.pack)
pack_into = mock_function("ustruct.pack_into", default_return=_struct.pack_into)
unpack = mock_function("ustruct.unpack", default_return=_struct.unpack)
unpack_from = mock_function("ustruct.unpack_from", default_return=_struct.unpack_from)
calcsize = mock_function("ustruct.calcsize", default_return=_struct.calcsize)


def __getattr__(name: str) -> Any:
    if hasattr(_struct, name):
        return getattr(_struct, name)
    raise AttributeError(f"module 'ustruct' has no attribute '{name}'")
