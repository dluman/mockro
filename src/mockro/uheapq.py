"""Mock implementation of the MicroPython ``uheapq`` module."""

from __future__ import annotations

import heapq as _heapq
from typing import Any

from mockro._factory import mock_function

heappush = mock_function("uheapq.heappush", default_return=_heapq.heappush)
heappop = mock_function("uheapq.heappop", default_return=_heapq.heappop)
heapify = mock_function("uheapq.heapify", default_return=_heapq.heapify)


def __getattr__(name: str) -> Any:
    if hasattr(_heapq, name):
        return getattr(_heapq, name)
    raise AttributeError(f"module 'uheapq' has no attribute '{name}'")
