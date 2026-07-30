"""Mock implementation of the MicroPython ``usocket`` module."""

from __future__ import annotations

from typing import Any

from mockro._factory import mock_class, mock_function

AF_INET = 2
AF_INET6 = 10
AF_UNIX = 1

SOCK_STREAM = 1
SOCK_DGRAM = 2
SOCK_RAW = 3

IPPROTO_TCP = 6
IPPROTO_UDP = 17
IPPROTO_IP = 0

SOL_SOCKET = 1
SO_REUSEADDR = 2

IPPROTO_SEC = 1  # ESP32 specific


@mock_class("usocket.socket")
class socket:
    """Mock network socket."""

    _init = mock_function("usocket.socket.__init__", default_return=None)
    _close = mock_function("usocket.socket.close", default_return=None)
    _bind = mock_function("usocket.socket.bind", default_return=None)
    _listen = mock_function("usocket.socket.listen", default_return=None)
    _accept = mock_function(
        "usocket.socket.accept", default_return=lambda: (socket(), ("127.0.0.1", 0))
    )
    _connect = mock_function("usocket.socket.connect", default_return=None)
    _send = mock_function("usocket.socket.send", default_return=0)
    _sendall = mock_function("usocket.socket.sendall", default_return=None)
    _sendto = mock_function("usocket.socket.sendto", default_return=0)
    _recv = mock_function(
        "usocket.socket.recv", default_return=lambda self, bufsize: b"\x00" * bufsize
    )
    _recvfrom = mock_function(
        "usocket.socket.recvfrom", default_return=lambda: (b"", ("0.0.0.0", 0))
    )
    _recvinto = mock_function("usocket.socket.recvinto", default_return=0)
    _setsockopt = mock_function("usocket.socket.setsockopt", default_return=None)
    _setblocking = mock_function("usocket.socket.setblocking", default_return=None)
    _settimeout = mock_function("usocket.socket.settimeout", default_return=None)
    _getaddrinfo = mock_function("usocket.socket.getaddrinfo", default_return=list)
    _makefile = mock_function("usocket.socket.makefile", default_return=lambda: None)
    _read = mock_function("usocket.socket.read", default_return=lambda self, size: b"")
    _readline = mock_function("usocket.socket.readline", default_return=b"")
    _write = mock_function("usocket.socket.write", default_return=0)

    def __init__(
        self,
        af: int = AF_INET,
        type: int = SOCK_STREAM,
        proto: int = 0,
        fileno: Any = None,
    ) -> None:
        self._init(self, af, type, proto, fileno)

    def close(self) -> None:
        self._close(self)

    def bind(self, address: Any) -> None:
        self._bind(self, address)

    def listen(self, backlog: int = 1) -> None:
        self._listen(self, backlog)

    def accept(self) -> tuple[Any, ...]:
        return self._accept(self)

    def connect(self, address: Any) -> None:
        self._connect(self, address)

    def send(self, bytes: bytes, flags: int = 0) -> int:
        return self._send(self, bytes, flags)

    def sendall(self, bytes: bytes, flags: int = 0) -> None:
        self._sendall(self, bytes, flags)

    def sendto(self, bytes: bytes, address: Any) -> int:
        return self._sendto(self, bytes, address)

    def recv(self, bufsize: int, flags: int = 0) -> bytes:
        return self._recv(self, bufsize, flags)

    def recvfrom(self, bufsize: int, flags: int = 0) -> tuple[Any, ...]:
        return self._recvfrom(self, bufsize, flags)

    def recvinto(self, buf: bytearray, nbytes: int = 0, flags: int = 0) -> int:
        return self._recvinto(self, buf, nbytes, flags)

    def setsockopt(self, level: int, optname: int, value: Any) -> None:
        self._setsockopt(self, level, optname, value)

    def setblocking(self, flag: bool) -> None:
        self._setblocking(self, flag)

    def settimeout(self, value: Any) -> None:
        self._settimeout(self, value)

    def getaddrinfo(
        self, host: str, port: int, af: int = 0, type: int = 0, proto: int = 0, flags: int = 0
    ) -> list[Any]:  # noqa: E501
        return self._getaddrinfo(self, host, port, af, type, proto, flags)

    def makefile(self, mode: str = "rb", buffering: int = 0, *args: Any) -> Any:
        return self._makefile(self, mode, buffering, *args)

    def read(self, size: int = -1) -> bytes:
        return self._read(self, size)

    def readline(self) -> bytes:
        return self._readline(self)

    def write(self, buf: bytes) -> int:
        return self._write(self, buf)

    def __enter__(self) -> socket:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


getaddrinfo = mock_function("usocket.getaddrinfo", default_return=list)
gethostbyname = mock_function("usocket.gethostbyname", default_return=lambda host: "0.0.0.0")
htons = mock_function("usocket.htons", default_return=lambda x: x)
ntohs = mock_function("usocket.ntohs", default_return=lambda x: x)
inet_aton = mock_function("usocket.inet_aton", default_return=lambda ip: b"\x00\x00\x00\x00")
inet_ntoa = mock_function("usocket.inet_ntoa", default_return=lambda packed: "0.0.0.0")


socket = socket  # Re-export the class under the module-level name as well.
