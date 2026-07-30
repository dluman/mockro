"""Mock implementation of the MicroPython ``uhashlib`` module."""

from __future__ import annotations

import hashlib as _hashlib
from typing import Any

from feign._factory import mock_class


class _MockHash:
    """Base class for mocked hash objects."""

    _digest_size: int = 0

    def __init__(self, data: bytes = b"") -> None:
        self._data = data

    def update(self, data: bytes) -> None:
        self._data += data

    def digest(self) -> bytes:
        return b"\x00" * self._digest_size

    def hexdigest(self) -> str:
        return "0" * (self._digest_size * 2)


@mock_class("uhashlib.md5")
class md5(_MockHash):
    _digest_size = 16


@mock_class("uhashlib.sha1")
class sha1(_MockHash):
    _digest_size = 20


@mock_class("uhashlib.sha256")
class sha256(_MockHash):
    _digest_size = 32


@mock_class("uhashlib.sha512")
class sha512(_MockHash):
    _digest_size = 64


def new(name: str, data: bytes = b"") -> Any:
    """Create a new hash object."""
    return _hashlib.new(name, data)
