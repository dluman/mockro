"""Mock implementation of the MicroPython ``ucollections`` module."""

from __future__ import annotations

from collections import OrderedDict as _OrderedDict
from collections import deque as _deque
from collections.abc import Callable
from typing import Any

from feign._factory import mock_class, mock_function


def namedtuple(name: str, fields: Any) -> Callable[..., Any]:
    """Create a namedtuple-like factory."""
    field_list = fields.replace(",", " ").split() if isinstance(fields, str) else list(fields)

    def factory(*values: Any) -> Any:
        values = values[: len(field_list)]
        return tuple.__new__(tuple, values)

    factory._fields = tuple(field_list)  # type: ignore[attr-defined]
    factory.__name__ = name
    factory.__doc__ = f"Mock namedtuple {name}"
    return mock_function(f"ucollections.namedtuple.{name}", default_return=factory)


OrderedDict = _OrderedDict
deque = _deque


@mock_class("ucollections.defaultdict")
class defaultdict(dict[Any, Any]):
    """Mock defaultdict."""

    def __init__(self, default_factory: Any = None, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __missing__(self, key: Any) -> Any:
        if self.default_factory is None:
            raise KeyError(key)
        value = self.default_factory()
        self[key] = value
        return value
