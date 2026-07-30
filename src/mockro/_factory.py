"""Factory helpers for creating mock functions and classes."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, cast

from mockro._core import MISSING, OverrideSpec, get_registry
from mockro._recorder import get_recorder


def mock_function(name: str, default_return: Any = None) -> Any:
    """Create a mock function that resolves overrides and records calls.

    Args:
        name: Fully-qualified dotted name, e.g. ``machine.Pin.value``.
        default_return: Value returned when no override is registered.  May be
            a callable that computes the default from arguments.

    Returns:
        A callable suitable for use as a module-level function or method.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        override = get_registry().get(name)
        if override is not MISSING:
            if isinstance(override, OverrideSpec):
                return override.to_callable()(*args, **kwargs)
            if callable(override):
                return override(*args, **kwargs)
            return override

        get_recorder().record(name, args, kwargs)

        if callable(default_return):
            return default_return(*args, **kwargs)
        return default_return

    wrapper.__name__ = name.split(".")[-1]
    wrapper.__doc__ = f"Mock implementation of {name}."
    return wrapper


def mock_class(name: str) -> Callable[[type], type]:
    """Create a class decorator that enables class-level overrides.

    The wrapper leaves normal instantiation untouched unless the registry
    contains a replacement for the class's dotted name, in which case the
    replacement is returned instead.
    """

    def decorator(cls: type) -> type:
        original_new = cast(Callable[..., Any], cls.__new__)

        def _new(cls_: type, *args: Any, **kwargs: Any) -> Any:
            override = get_registry().get(name)
            if override is not MISSING:
                if isinstance(override, OverrideSpec):
                    return override.to_callable()(*args, **kwargs)
                if callable(override):
                    return override(*args, **kwargs)
                return override
            return original_new(cls_)

        cls.__new__ = _new  # type: ignore[assignment]
        return cls

    return decorator
