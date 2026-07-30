"""Compatibility alias for ``mockro.usocket``."""

from mockro.usocket import (  # noqa: F401
    AF_INET,
    AF_INET6,
    AF_UNIX,
    IPPROTO_IP,
    IPPROTO_SEC,
    IPPROTO_TCP,
    IPPROTO_UDP,
    SO_REUSEADDR,
    SOCK_DGRAM,
    SOCK_RAW,
    SOCK_STREAM,
    SOL_SOCKET,
    getaddrinfo,
    gethostbyname,
    htons,
    inet_aton,
    inet_ntoa,
    ntohs,
    socket,
)
