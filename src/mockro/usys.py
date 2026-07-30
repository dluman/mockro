"""Mock implementation of the MicroPython ``usys`` module."""

from __future__ import annotations

import sys as _sys
from typing import Any

from mockro._factory import mock_function

stdin = _sys.stdin
stdout = _sys.stdout
stderr = _sys.stderr
argv: list[str] = []
path: list[str] = []
modules: dict[str, Any] = {}
platform = "micropython"
version = "3.4.0"
version_info = (3, 4, 0, "final", 0)
implementation = (
    "micropython",
    (1, 20, 0),
    0,
)
byteorder = "little"
maxsize = 2147483647

exit = mock_function("usys.exit", default_return=_sys.exit)
print_exception = mock_function(
    "usys.print_exception", default_return=lambda exc, stream=None: None
)


class _ExcInfo:
    def __init__(self, exc: Any) -> None:
        self.exc = exc

    def __enter__(self) -> Any:
        return self.exc

    def __exit__(self, *args: Any) -> bool:
        return True


_exc_info = mock_function("usys.exc_info", default_return=lambda: (None, None, None))


def exc_info() -> Any:
    return _exc_info()
