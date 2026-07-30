"""Mock implementation of the SAMD-specific ``samd`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_function

chip_id = mock_function("samd.chip_id", default_return=lambda: b"\x00" * 16)
serial_number = mock_function("samd.serial_number", default_return=lambda: b"\x00" * 16)
reset_reason = mock_function("samd.reset_reason", default_return=0)


def __getattr__(name: str) -> Any:
    if name in (
        "RESET_REASON_POR",
        "RESET_REASON_BOD12",
        "RESET_REASON_BOD33",
        "RESET_REASON_EXT",
        "RESET_REASON_WDT",
        "RESET_REASON_SYST",
    ):
        return 0
    raise AttributeError(f"module 'samd' has no attribute '{name}'")
