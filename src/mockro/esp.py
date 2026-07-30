"""Mock implementation of the ESP8266-specific ``esp`` module."""

from __future__ import annotations

from typing import Any

from mockro._factory import mock_function

sleep_type = mock_function("esp.sleep_type", default_return=0)
sleep_disable = mock_function("esp.sleep_disable", default_return=None)
sleep_light = mock_function("esp.sleep_light", default_return=None)
sleep_deep = mock_function("esp.sleep_deep", default_return=None)

flash_read = mock_function("esp.flash_read", default_return=None)
flash_write = mock_function("esp.flash_write", default_return=None)
flash_erase = mock_function("esp.flash_erase", default_return=None)
flash_size = mock_function("esp.flash_size", default_return=4 * 1024 * 1024)

osdebug = mock_function("esp.osdebug", default_return=None)


def __getattr__(name: str) -> Any:
    if name in ("SLEEP_NONE", "SLEEP_LIGHT", "SLEEP_MODEM"):
        return 0
    raise AttributeError(f"module 'esp' has no attribute '{name}'")
