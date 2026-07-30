"""Mock implementation of the MicroPython ``uzlib`` module."""

from __future__ import annotations

import zlib as _zlib

from feign._factory import mock_function

decompress = mock_function("uzlib.decompress", default_return=_zlib.decompress)
compress = mock_function("uzlib.compress", default_return=_zlib.compress)
crc32 = mock_function("uzlib.crc32", default_return=_zlib.crc32)


class Adler32:
    """Mock Adler32 checksum object."""

    def __init__(self, data: bytes = b"") -> None:
        self._value = 1
        if data:
            self.update(data)

    def update(self, data: bytes) -> None:
        self._value = _zlib.adler32(data, self._value)

    def digest(self) -> int:
        return self._value


adler32 = mock_function("uzlib.adler32", default_return=_zlib.adler32)
