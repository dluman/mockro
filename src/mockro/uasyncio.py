"""Mock implementation of the MicroPython ``uasyncio`` module."""

from __future__ import annotations

import asyncio as _asyncio
from typing import Any

from mockro._factory import mock_class, mock_function

sleep = mock_function("uasyncio.sleep", default_return=_asyncio.sleep)
sleep_ms = mock_function("uasyncio.sleep_ms", default_return=lambda ms: _asyncio.sleep(ms / 1000))
gather = mock_function("uasyncio.gather", default_return=_asyncio.gather)
wait_for = mock_function("uasyncio.wait_for", default_return=_asyncio.wait_for)
wait_for_ms = mock_function("uasyncio.wait_for_ms", default_return=lambda coro, timeout: coro)


@mock_class("uasyncio.Event")
class Event:
    """Mock asyncio event."""

    _init = mock_function("uasyncio.Event.__init__", default_return=None)
    _is_set = mock_function("uasyncio.Event.is_set", default_return=False)
    _set = mock_function("uasyncio.Event.set", default_return=None)
    _clear = mock_function("uasyncio.Event.clear", default_return=None)
    _wait = mock_function("uasyncio.Event.wait", default_return=None)

    def __init__(self) -> None:
        self._init(self)

    def is_set(self) -> bool:
        return self._is_set(self)

    def set(self) -> None:
        self._set(self)

    def clear(self) -> None:
        self._clear(self)

    async def wait(self) -> None:
        return await self._wait(self)


@mock_class("uasyncio.Lock")
class Lock:
    """Mock asyncio lock."""

    _init = mock_function("uasyncio.Lock.__init__", default_return=None)
    _locked = mock_function("uasyncio.Lock.locked", default_return=False)
    _acquire = mock_function("uasyncio.Lock.acquire", default_return=True)
    _release = mock_function("uasyncio.Lock.release", default_return=None)

    def __init__(self) -> None:
        self._init(self)

    def locked(self) -> bool:
        return self._locked(self)

    async def acquire(self) -> bool:
        return await self._acquire(self)

    def release(self) -> None:
        self._release(self)

    async def __aenter__(self) -> Lock:
        await self.acquire()
        return self

    async def __aexit__(self, *args: Any) -> None:
        self.release()


@mock_class("uasyncio.StreamReader")
class StreamReader:
    """Mock asyncio stream reader."""

    _init = mock_function("uasyncio.StreamReader.__init__", default_return=None)
    _read = mock_function("uasyncio.StreamReader.read", default_return=lambda self, n: b"")
    _readline = mock_function("uasyncio.StreamReader.readline", default_return=b"")
    _readexactly = mock_function(
        "uasyncio.StreamReader.readexactly", default_return=lambda self, n: b"\x00" * n
    )
    _wait_closed = mock_function("uasyncio.StreamReader.wait_closed", default_return=None)

    def __init__(self) -> None:
        self._init(self)

    async def read(self, n: int = -1) -> bytes:
        return await self._read(self, n)

    async def readline(self) -> bytes:
        return await self._readline(self)

    async def readexactly(self, n: int) -> bytes:
        return await self._readexactly(self, n)

    async def wait_closed(self) -> None:
        await self._wait_closed(self)


@mock_class("uasyncio.StreamWriter")
class StreamWriter:
    """Mock asyncio stream writer."""

    _init = mock_function("uasyncio.StreamWriter.__init__", default_return=None)
    _write = mock_function("uasyncio.StreamWriter.write", default_return=None)
    _drain = mock_function("uasyncio.StreamWriter.drain", default_return=None)
    _close = mock_function("uasyncio.StreamWriter.close", default_return=None)
    _wait_closed = mock_function("uasyncio.StreamWriter.wait_closed", default_return=None)
    _get_extra_info = mock_function("uasyncio.StreamWriter.get_extra_info", default_return=None)

    def __init__(self) -> None:
        self._init(self)

    def write(self, buf: bytes) -> None:
        self._write(self, buf)

    async def drain(self) -> None:
        await self._drain(self)

    def close(self) -> None:
        self._close(self)

    async def wait_closed(self) -> None:
        await self._wait_closed(self)

    def get_extra_info(self, name: str, default: Any = None) -> Any:
        return self._get_extra_info(self, name, default)

    async def __aenter__(self) -> StreamWriter:
        return self

    async def __aexit__(self, *args: Any) -> None:
        self.close()
        await self.wait_closed()


@mock_class("uasyncio.Task")
class Task:
    """Mock asyncio task."""

    _init = mock_function("uasyncio.Task.__init__", default_return=None)
    _cancel = mock_function("uasyncio.Task.cancel", default_return=False)

    def __init__(self, coro: Any) -> None:
        self._init(self, coro)

    def cancel(self) -> bool:
        return self._cancel(self)


def create_task(coro: Any) -> Task:
    """Create a mock task."""
    return Task(coro)


def run(coro: Any) -> Any:
    """Run a coroutine in the mocked async runtime."""
    return _asyncio.run(coro)


open_connection = mock_function(
    "uasyncio.open_connection",
    default_return=lambda host, port: (StreamReader(), StreamWriter()),
)
start_server = mock_function(
    "uasyncio.start_server",
    default_return=lambda callback, host, port: None,
)


@mock_class("uasyncio.ThreadSafeFlag")
class ThreadSafeFlag:
    """Mock thread-safe flag."""

    _set = mock_function("uasyncio.ThreadSafeFlag.set", default_return=None)
    _wait = mock_function("uasyncio.ThreadSafeFlag.wait", default_return=None)

    def set(self) -> None:
        self._set(self)

    async def wait(self) -> None:
        await self._wait(self)


@mock_class("uasyncio.Semaphore")
class Semaphore:
    """Mock asyncio semaphore."""

    _init = mock_function("uasyncio.Semaphore.__init__", default_return=None)
    _acquire = mock_function("uasyncio.Semaphore.acquire", default_return=True)
    _release = mock_function("uasyncio.Semaphore.release", default_return=None)

    def __init__(self, value: int = 1) -> None:
        self._init(self, value)

    async def acquire(self) -> bool:
        return await self._acquire(self)

    def release(self) -> None:
        self._release(self)


@mock_class("uasyncio.Queue")
class Queue:
    """Mock asyncio queue."""

    _init = mock_function("uasyncio.Queue.__init__", default_return=None)
    _put = mock_function("uasyncio.Queue.put", default_return=None)
    _get = mock_function("uasyncio.Queue.get", default_return=None)
    _empty = mock_function("uasyncio.Queue.empty", default_return=True)
    _full = mock_function("uasyncio.Queue.full", default_return=False)

    def __init__(self, maxsize: int = 0) -> None:
        self._init(self, maxsize)

    async def put(self, item: Any) -> None:
        await self._put(self, item)

    async def get(self) -> Any:
        return await self._get(self)

    def empty(self) -> bool:
        return self._empty(self)

    def full(self) -> bool:
        return self._full(self)


Loop = _asyncio.AbstractEventLoop
new_event_loop = _asyncio.new_event_loop
get_event_loop = _asyncio.get_event_loop
