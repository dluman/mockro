"""Call recording for mocked functions and methods."""

from __future__ import annotations

from typing import Any


class Recorder:
    """Records invocations of mocked objects.

    The recorder is optional and lightweight. It stores the positional and
    keyword arguments passed to each named mock so that tests and assignments
    can assert that hardware interactions happened as expected.
    """

    def __init__(self) -> None:
        self._calls: dict[str, list[tuple[tuple[Any, ...], dict[str, Any]]]] = {}

    def record(
        self,
        name: str,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> None:
        """Store a call made to the named mock."""
        self._calls.setdefault(name, []).append((args, kwargs))

    def calls(self, name: str) -> list[tuple[tuple[Any, ...], dict[str, Any]]]:
        """Return all recorded calls for a named mock."""
        return list(self._calls.get(name, []))

    def clear(self) -> None:
        """Drop all recorded calls."""
        self._calls.clear()


_global_recorder = Recorder()


def get_recorder() -> Recorder:
    """Return the process-wide recorder."""
    return _global_recorder
