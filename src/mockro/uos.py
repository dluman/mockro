"""Mock implementation of the MicroPython ``uos`` module."""

from __future__ import annotations

import os as _os
from typing import Any

from mockro._factory import mock_function

uname = mock_function(
    "uos.uname",
    default_return=lambda: (
        "sysname",
        "nodename",
        "release",
        "version",
        "machine",
    ),
)
urandom = mock_function("uos.urandom", default_return=lambda n: b"\x00" * n)
chdir = mock_function("uos.chdir", default_return=_os.chdir)
getcwd = mock_function("uos.getcwd", default_return=lambda: "/")
listdir = mock_function("uos.listdir", default_return=lambda: [])
mkdir = mock_function("uos.mkdir", default_return=lambda name: None)
remove = mock_function("uos.remove", default_return=lambda name: None)
rename = mock_function("uos.rename", default_return=lambda old, new: None)
rmdir = mock_function("uos.rmdir", default_return=lambda name: None)
stat = mock_function("uos.stat", default_return=lambda path: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
statvfs = mock_function("uos.statvfs", default_return=lambda path: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
sync = mock_function("uos.sync", default_return=None)

dupterm = mock_function("uos.dupterm", default_return=lambda stream, *args: None)

mount = mock_function("uos.mount", default_return=None)
umount = mock_function("uos.umount", default_return=None)


def __getattr__(name: str) -> Any:
    if name == "VfsFat":
        return mock_function("uos.VfsFat", default_return=lambda: None)
    if name == "VfsLfs2":
        return mock_function("uos.VfsLfs2", default_return=lambda: None)
    raise AttributeError(f"module 'uos' has no attribute '{name}'")
