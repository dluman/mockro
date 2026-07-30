"""Mock implementation of the MicroPython ``uselect`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function


@mock_class("uselect.poll")
class poll:
    """Mock poll object."""

    _init = mock_function("uselect.poll.__init__", default_return=None)
    _register = mock_function("uselect.poll.register", default_return=None)
    _unregister = mock_function("uselect.poll.unregister", default_return=None)
    _modify = mock_function("uselect.poll.modify", default_return=None)
    _poll = mock_function("uselect.poll.poll", default_return=list)
    _ipoll = mock_function("uselect.poll.ipoll", default_return=iter([]))

    def __init__(self) -> None:
        self._init(self)

    def register(self, obj: Any, eventmask: int = 1) -> None:
        self._register(self, obj, eventmask)

    def unregister(self, obj: Any) -> None:
        self._unregister(self, obj)

    def modify(self, obj: Any, eventmask: int = 1) -> None:
        self._modify(self, obj, eventmask)

    def poll(self, timeout: int = -1) -> list[Any]:
        return self._poll(self, timeout)

    def ipoll(self, timeout: int = -1, flags: int = 0) -> Any:
        return self._ipoll(self, timeout, flags)


select = mock_function("uselect.select", default_return=lambda r, w, x, timeout=None: ([], [], []))


POLLIN = 1
POLLOUT = 2
POLLERR = 4
POLLHUP = 8
