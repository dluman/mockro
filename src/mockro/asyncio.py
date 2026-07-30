"""Compatibility alias for ``mockro.uasyncio``."""

from mockro.uasyncio import (  # noqa: F401
    Event,
    Lock,
    Loop,
    Queue,
    Semaphore,
    StreamReader,
    StreamWriter,
    Task,
    ThreadSafeFlag,
    create_task,
    gather,
    get_event_loop,
    new_event_loop,
    open_connection,
    run,
    sleep,
    sleep_ms,
    start_server,
    wait_for,
    wait_for_ms,
)
