"""Mock implementation of the MicroPython ``utime`` module."""

from __future__ import annotations

import time as _time

from feign._factory import mock_function

sleep = mock_function("utime.sleep", default_return=_time.sleep)
sleep_ms = mock_function("utime.sleep_ms", default_return=lambda ms: None)
sleep_us = mock_function("utime.sleep_us", default_return=lambda us: None)
ticks_ms = mock_function("utime.ticks_ms", default_return=lambda: int(_time.time() * 1000))
ticks_us = mock_function("utime.ticks_us", default_return=lambda: int(_time.time() * 1_000_000))
ticks_cpu = mock_function("utime.ticks_cpu", default_return=lambda: int(_time.time() * 1_000_000))
ticks_add = mock_function("utime.ticks_add", default_return=lambda ticks, delta: ticks + delta)
ticks_diff = mock_function(
    "utime.ticks_diff", default_return=lambda ticks1, ticks2: ticks1 - ticks2
)
time = mock_function("utime.time", default_return=_time.time)
localtime = mock_function("utime.localtime", default_return=_time.localtime)
gmtime = mock_function("utime.gmtime", default_return=_time.gmtime)
mktime = mock_function("utime.mktime", default_return=_time.mktime)
