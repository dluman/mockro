"""Mock implementation of the MicroPython ``gc`` module."""

from __future__ import annotations

from feign._factory import mock_function

collect = mock_function("gc.collect", default_return=0)
disable = mock_function("gc.disable", default_return=None)
enable = mock_function("gc.enable", default_return=None)
isenabled = mock_function("gc.isenabled", default_return=True)
mem_free = mock_function("gc.mem_free", default_return=1_000_000)
mem_alloc = mock_function("gc.mem_alloc", default_return=100_000)
mem_total = mock_function("gc.mem_total", default_return=1_100_000)
threshold = mock_function("gc.threshold", default_return=lambda *args: 0)
