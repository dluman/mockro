"""Mock implementation of the MicroPython ``neopixel`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function


@mock_class("neopixel.NeoPixel")
class NeoPixel:
    """Mock NeoPixel / WS2812 LED driver."""

    _init = mock_function("neopixel.NeoPixel.__init__", default_return=None)
    _write = mock_function("neopixel.NeoPixel.write", default_return=None)
    _fill = mock_function("neopixel.NeoPixel.fill", default_return=None)

    def __init__(
        self,
        pin: Any,
        n: int,
        *,
        bpp: int = 3,
        timing: int = 1,
    ) -> None:
        self._init(self, pin, n, bpp=bpp, timing=timing)
        self._buffer = [(0, 0, 0)] * n
        self.n = n

    def __setitem__(self, index: int, val: Any) -> None:
        self._buffer[index] = val

    def __getitem__(self, index: int) -> Any:
        return self._buffer[index]

    def __len__(self) -> int:
        return self.n

    def write(self) -> None:
        self._write(self)

    def fill(self, color: Any) -> None:
        self._fill(self, color)
        self._buffer = [color] * self.n
