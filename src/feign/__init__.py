"""feign: Mock MicroPython libraries for CPython development and testing."""

from __future__ import annotations

from feign._core import (
    activate,
    override,
    patch,
)
from feign._factory import mock_class, mock_function
from feign._recorder import get_recorder

__version__ = "0.1.0"

__all__ = [
    "activate",
    "patch",
    "override",
    "get_recorder",
    "mock_function",
    "mock_class",
]
