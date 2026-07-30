"""Mock implementation of the MicroPython ``ujson`` module."""

from __future__ import annotations

import json as _json
from typing import Any

from feign._factory import mock_function

dumps = mock_function("ujson.dumps", default_return=_json.dumps)
dump = mock_function("ujson.dump", default_return=_json.dump)
loads = mock_function("ujson.loads", default_return=_json.loads)
load = mock_function("ujson.load", default_return=_json.load)


def __getattr__(name: str) -> Any:
    if name == "JSONDecodeError":
        return _json.JSONDecodeError
    raise AttributeError(f"module 'ujson' has no attribute '{name}'")
