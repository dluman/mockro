"""Mock implementation of the MicroPython ``ubinascii`` module."""

from __future__ import annotations

import binascii as _binascii
from typing import Any

from feign._factory import mock_function

hexlify = mock_function("ubinascii.hexlify", default_return=_binascii.hexlify)
unhexlify = mock_function("ubinascii.unhexlify", default_return=_binascii.unhexlify)
a2b_base64 = mock_function("ubinascii.a2b_base64", default_return=_binascii.a2b_base64)
b2a_base64 = mock_function("ubinascii.b2a_base64", default_return=_binascii.b2a_base64)
crc32 = mock_function("ubinascii.crc32", default_return=_binascii.crc32)
crc_hqx = mock_function("ubinascii.crc_hqx", default_return=lambda data, crc: 0)
b2a_qp = mock_function("ubinascii.b2a_qp", default_return=lambda data: b"")
a2b_qp = mock_function("ubinascii.a2b_qp", default_return=lambda data: b"")


def __getattr__(name: str) -> Any:
    if name == "Error":
        return _binascii.Error
    raise AttributeError(f"module 'ubinascii' has no attribute '{name}'")
