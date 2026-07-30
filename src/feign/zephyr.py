"""Mock implementation of the Zephyr-specific ``zephyr`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_function

discharge = mock_function("zephyr.discharge", default_return=None)
shell_exec = mock_function("zephyr.shell_exec", default_return=0)


def __getattr__(name: str) -> Any:
    if name in ("DISCHARGE_*",):
        return 0
    raise AttributeError(f"module 'zephyr' has no attribute '{name}'")
