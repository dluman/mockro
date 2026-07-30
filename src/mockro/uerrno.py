"""Mock implementation of the MicroPython ``uerrno`` module."""

from __future__ import annotations

import errno as _errno
from typing import Any

EEXIST = _errno.EEXIST
ENOENT = _errno.ENOENT
EINVAL = _errno.EINVAL
EIO = _errno.EIO
EACCES = _errno.EACCES
EAGAIN = _errno.EAGAIN
ENOMEM = _errno.ENOMEM
ENODEV = _errno.ENODEV
ENOTDIR = _errno.ENOTDIR
EISDIR = _errno.EISDIR

errorcode = {v: k for k, v in _errno.__dict__.items() if isinstance(v, int)}


def __getattr__(name: str) -> Any:
    if hasattr(_errno, name):
        return getattr(_errno, name)
    raise AttributeError(f"module 'uerrno' has no attribute '{name}'")
