"""mockro: Mock MicroPython libraries for CPython development and testing."""

from __future__ import annotations

from mockro._core import (
    activate,
    override,
    patch,
)
from mockro._factory import mock_class, mock_function
from mockro._recorder import get_recorder

__version__ = "0.1.0"

__all__ = [
    "activate",
    "patch",
    "override",
    "get_recorder",
    "mock_function",
    "mock_class",
]
