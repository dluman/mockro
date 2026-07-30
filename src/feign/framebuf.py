"""Mock implementation of the MicroPython ``framebuf`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function

MONO_VLSB = 0
MONO_HLSB = 1
MONO_HMSB = 2
RGB565 = 3
GS2_HMSB = 4
GS4_HMSB = 5
GS8 = 6


@mock_class("framebuf.FrameBuffer")
class FrameBuffer:
    """Mock frame buffer for small displays."""

    _init = mock_function("framebuf.FrameBuffer.__init__", default_return=None)
    _fill = mock_function("framebuf.FrameBuffer.fill", default_return=None)
    _pixel = mock_function("framebuf.FrameBuffer.pixel", default_return=0)
    _hline = mock_function("framebuf.FrameBuffer.hline", default_return=None)
    _vline = mock_function("framebuf.FrameBuffer.vline", default_return=None)
    _line = mock_function("framebuf.FrameBuffer.line", default_return=None)
    _rect = mock_function("framebuf.FrameBuffer.rect", default_return=None)
    _fill_rect = mock_function("framebuf.FrameBuffer.fill_rect", default_return=None)
    _text = mock_function("framebuf.FrameBuffer.text", default_return=None)
    _scroll = mock_function("framebuf.FrameBuffer.scroll", default_return=None)
    _blit = mock_function("framebuf.FrameBuffer.blit", default_return=None)
    _draw_rect = mock_function("framebuf.FrameBuffer.draw_rect", default_return=None)

    def __init__(self, buffer: Any, width: int, height: int, format: int, stride: int = 0) -> None:
        self._init(self, buffer, width, height, format, stride)
        self.width = width
        self.height = height

    def fill(self, c: int) -> None:
        self._fill(self, c)

    def pixel(self, x: int, y: int, c: int | None = None) -> Any:
        return self._pixel(self, x, y, c)

    def hline(self, x: int, y: int, w: int, c: int) -> None:
        self._hline(self, x, y, w, c)

    def vline(self, x: int, y: int, h: int, c: int) -> None:
        self._vline(self, x, y, h, c)

    def line(self, x1: int, y1: int, x2: int, y2: int, c: int) -> None:
        self._line(self, x1, y1, x2, y2, c)

    def rect(self, x: int, y: int, w: int, h: int, c: int) -> None:
        self._rect(self, x, y, w, h, c)

    def fill_rect(self, x: int, y: int, w: int, h: int, c: int) -> None:
        self._fill_rect(self, x, y, w, h, c)

    def text(self, s: str, x: int, y: int, c: int = 1) -> None:
        self._text(self, s, x, y, c)

    def scroll(self, xstep: int, ystep: int) -> None:
        self._scroll(self, xstep, ystep)

    def blit(self, fbuf: Any, x: int, y: int, key: int = -1, palette: Any = None) -> None:
        self._blit(self, fbuf, x, y, key, palette)

    def draw_rect(self, x: int, y: int, w: int, h: int, c: int) -> None:
        self._draw_rect(self, x, y, w, h, c)


Font = mock_function("framebuf.Font", default_return=lambda: None)
