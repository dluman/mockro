"""Core registry, activation, and patching machinery."""

from __future__ import annotations

import importlib
import os
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any


class _Missing:
    """Sentinel value for optional arguments."""

    def __repr__(self) -> str:  # pragma: no cover
        return "MISSING"


MISSING = _Missing()


@dataclass
class OverrideSpec:
    """Description of how a mock should behave when invoked."""

    return_value: Any = MISSING
    side_effect: Any = MISSING

    def __post_init__(self) -> None:
        self._side_effect_iterator: _IterableSideEffect | None = None

    def to_callable(self) -> Any:
        """Return a callable that realizes this override."""
        if self.side_effect is not MISSING:
            if callable(self.side_effect):
                return self.side_effect
            if self._side_effect_iterator is None:
                self._side_effect_iterator = _IterableSideEffect(self.side_effect)
            return self._side_effect_iterator
        if self.return_value is not MISSING:
            return lambda *args, **kwargs: self.return_value
        return lambda *args, **kwargs: None


class _IterableSideEffect:
    """Turns an iterable into a callable that yields the next value each call."""

    def __init__(self, iterable: Any) -> None:
        self._iterator = iter(iterable)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        try:
            return next(self._iterator)
        except StopIteration as exc:
            raise RuntimeError("side_effect iterator is exhausted") from exc


class Registry:
    """Stores overrides and applies class-level replacements."""

    def __init__(self) -> None:
        self._overrides: dict[str, Any] = {}
        self._class_backups: dict[str, Any] = {}

    def set(self, target: str, override: Any) -> None:
        """Register an override and apply class-level replacements directly."""
        self._overrides[target] = override

        # If the target looks like a class on a module (exactly one dot),
        # replace the attribute on the module so ``module.Class`` resolves
        # to the override.
        if target.count(".") == 1:
            module_name, attr = target.split(".")
            module = sys.modules.get(module_name)
            if module is not None and hasattr(module, attr):
                self._class_backups.setdefault(target, getattr(module, attr))
                setattr(module, attr, override)

    def get(self, target: str) -> Any:
        """Return the override for a target, or MISSING."""
        return self._overrides.get(target, MISSING)

    def remove(self, target: str) -> None:
        """Remove an override and restore any class-level replacement."""
        self._overrides.pop(target, None)
        if target in self._class_backups:
            module_name, attr = target.split(".")
            module = sys.modules.get(module_name)
            if module is not None:
                setattr(module, attr, self._class_backups[target])
            del self._class_backups[target]

    def snapshot(self) -> dict[str, Any]:
        """Return a shallow copy of current overrides."""
        return dict(self._overrides)

    def restore(self, snapshot: dict[str, Any]) -> None:
        """Restore the registry to a previous snapshot."""
        for target in list(self._overrides):
            if target not in snapshot:
                self.remove(target)
        for target, override in snapshot.items():
            self.set(target, override)


_global_registry = Registry()


def get_registry() -> Registry:
    """Return the process-wide override registry."""
    return _global_registry


def _resolve_override(override: Any) -> Any:
    """Convert a registered override into a callable."""
    if isinstance(override, OverrideSpec):
        return override.to_callable()
    if callable(override):
        return override
    return lambda *args, **kwargs: override


# Modules that feign knows how to mock.  The list intentionally covers the full
# MicroPython standard library plus common port-specific modules.
#
# ``_SAFE_MODULE_NAMES`` are names that do not shadow CPython standard-library
# modules, so they can be installed safely even while pytest and other tooling
# are running.  ``_ALIAS_MODULE_NAMES`` are the non-u aliases that *do* shadow
# CPython stdlib modules; they are only installed when explicitly requested
# (e.g. via ``feign run``) so that tooling like pytest/asyncio keeps working.
_SAFE_MODULE_NAMES: tuple[str, ...] = (
    "machine",
    "network",
    "usocket",
    "utime",
    "uos",
    "usys",
    "ujson",
    "ubinascii",
    "uhashlib",
    "uerrno",
    "uheapq",
    "uasyncio",
    "uctypes",
    "ucollections",
    "ustruct",
    "uselect",
    "uzlib",
    "bluetooth",
    "framebuf",
    "gc",
    "micropython",
    "neopixel",
    "dht",
    "onewire",
    "ds18x20",
    "esp",
    "esp32",
    "rp2",
    "pyb",
    "samd",
    "zephyr",
)

_ALIAS_MODULE_NAMES: tuple[str, ...] = (
    "socket",
    "time",
    "os",
    "sys",
    "json",
    "binascii",
    "hashlib",
    "errno",
    "heapq",
    "asyncio",
    "ctypes",
    "collections",
    "struct",
    "select",
    "zlib",
)


def activate(aliases: bool = False) -> None:
    """Install feign's mock modules into ``sys.modules`` under MicroPython names.

    This makes ``import machine``, ``import network``, and similar statements
    resolve to feign's mocks in the current process.  The function is safe to
    call multiple times.

    Args:
        aliases: If ``True``, also install non-u aliases such as ``socket``,
            ``time``, ``os``, etc.  These shadow CPython standard-library
            modules, so they are disabled by default and should only be used
            when running an isolated MicroPython script (e.g. ``feign run``).
    """
    names = _SAFE_MODULE_NAMES
    if aliases:
        names = names + _ALIAS_MODULE_NAMES

    for name in names:
        try:
            module = importlib.import_module(f"feign.{name}")
        except ImportError:
            continue
        existing = sys.modules.get(name)
        if existing is module:
            continue
        sys.modules[name] = module


def patch(
    target: str,
    obj: Any = MISSING,
    *,
    return_value: Any = MISSING,
    side_effect: Any = MISSING,
) -> None:
    """Override a mocked function, method, or class.

    Args:
        target: Dotted name such as ``machine.Pin.value`` or ``machine.freq``.
        obj: Replacement object, callable, or constant value.  Mutually
            exclusive with ``return_value`` and ``side_effect``.
        return_value: Make the target always return this value.
        side_effect: A callable to invoke, or an iterable whose values are
            returned one per call.
    """
    if obj is not MISSING and (return_value is not MISSING or side_effect is not MISSING):
        raise TypeError("Cannot specify both 'obj' and 'return_value'/'side_effect'")

    if obj is not MISSING:
        override = obj
    elif return_value is not MISSING or side_effect is not MISSING:
        override = OverrideSpec(return_value=return_value, side_effect=side_effect)
    else:
        raise TypeError("Must specify one of 'obj', 'return_value', or 'side_effect'")

    get_registry().set(target, override)


@contextmanager
def override(**targets: Any) -> Iterator[None]:
    """Temporarily override mocks for a block of code.

    Keyword argument names use underscores in place of dots, so
    ``machine_Pin_value=1`` becomes the override ``machine.Pin.value``.
    """
    registry = get_registry()
    snapshot = registry.snapshot()
    try:
        for key, value in targets.items():
            target = key.replace("_", ".")
            patch(target, value)
        yield
    finally:
        registry.restore(snapshot)


def _maybe_activate_from_env() -> None:
    """Activate mocks when the ``FEIGN`` environment variable is set."""
    if os.environ.get("FEIGN"):
        activate(aliases=True)
