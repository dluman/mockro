"""Mock implementation of the MicroPython ``network`` module."""

from __future__ import annotations

from typing import Any

from mockro._factory import mock_class, mock_function

STA_IF = 0
AP_IF = 1

AUTH_OPEN = 0
AUTH_WEP = 1
AUTH_WPA_PSK = 2
AUTH_WPA2_PSK = 3
AUTH_WPA_WPA2_PSK = 4
AUTH_WPA3_PSK = 5
AUTH_WPA2_WPA3_PSK = 6

PHY_LAN8720 = 0
PHY_TLK110 = 1
PHY_IP101 = 2
PHY_RTL8201 = 3
PHY_DP83848 = 4


@mock_class("network.WLAN")
class WLAN:
    """Mock WiFi interface."""

    _init = mock_function("network.WLAN.__init__", default_return=None)
    _active = mock_function("network.WLAN.active", default_return=False)
    _connect = mock_function("network.WLAN.connect", default_return=None)
    _disconnect = mock_function("network.WLAN.disconnect", default_return=None)
    _scan = mock_function("network.WLAN.scan", default_return=list)
    _isconnected = mock_function("network.WLAN.isconnected", default_return=False)
    _ifconfig = mock_function(
        "network.WLAN.ifconfig", default_return=lambda: ("0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0")
    )
    _config = mock_function("network.WLAN.config", default_return=None)
    _status = mock_function("network.WLAN.status", default_return=0)
    _mac = mock_function("network.WLAN.mac", default_return=lambda: b"\x00" * 6)

    def __init__(self, interface_id: int = STA_IF) -> None:
        self._init(self, interface_id)

    def active(self, is_active: Any = None) -> Any:
        return self._active(self, is_active)

    def connect(self, ssid: Any = None, key: Any = None, *args: Any, **kwargs: Any) -> None:
        self._connect(self, ssid, key, *args, **kwargs)

    def disconnect(self) -> None:
        self._disconnect(self)

    def scan(self) -> list[Any]:
        return self._scan(self)

    def isconnected(self) -> bool:
        return self._isconnected(self)

    def ifconfig(self, config: Any = None) -> Any:
        return self._ifconfig(self, config)

    def config(self, *args: Any, **kwargs: Any) -> Any:
        return self._config(self, *args, **kwargs)

    def status(self, param: Any = None) -> Any:
        return self._status(self, param)

    def mac(self) -> bytes:
        return self._mac(self)


@mock_class("network.LAN")
class LAN:
    """Mock Ethernet interface."""

    _init = mock_function("network.LAN.__init__", default_return=None)
    _active = mock_function("network.LAN.active", default_return=False)
    _isconnected = mock_function("network.LAN.isconnected", default_return=False)
    _ifconfig = mock_function(
        "network.LAN.ifconfig", default_return=lambda: ("0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0")
    )
    _config = mock_function("network.LAN.config", default_return=None)

    def __init__(
        self,
        id: Any = 0,
        *,
        phy_type: Any = None,
        phy_addr: int = 0,
        mdc: Any = None,
        mdio: Any = None,
    ) -> None:  # noqa: E501
        self._init(self, id, phy_type=phy_type, phy_addr=phy_addr, mdc=mdc, mdio=mdio)

    def active(self, is_active: Any = None) -> Any:
        return self._active(self, is_active)

    def isconnected(self) -> bool:
        return self._isconnected(self)

    def ifconfig(self, config: Any = None) -> Any:
        return self._ifconfig(self, config)

    def config(self, *args: Any, **kwargs: Any) -> Any:
        return self._config(self, *args, **kwargs)


@mock_class("network.AbstractNIC")
class AbstractNIC:
    """Mock abstract network interface."""

    _active = mock_function("network.AbstractNIC.active", default_return=False)
    _isconnected = mock_function("network.AbstractNIC.isconnected", default_return=False)
    _ifconfig = mock_function(
        "network.AbstractNIC.ifconfig",
        default_return=lambda: ("0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0"),
    )

    def active(self, is_active: Any = None) -> Any:
        return self._active(self, is_active)

    def isconnected(self) -> bool:
        return self._isconnected(self)

    def ifconfig(self, config: Any = None) -> Any:
        return self._ifconfig(self, config)


@mock_class("network.Bluetooth")
class Bluetooth:
    """Mock network Bluetooth interface."""

    _init = mock_function("network.Bluetooth.__init__", default_return=None)
    _active = mock_function("network.Bluetooth.active", default_return=False)
    _config = mock_function("network.Bluetooth.config", default_return=None)

    def __init__(self, id: int = 0) -> None:
        self._init(self, id)

    def active(self, is_active: Any = None) -> Any:
        return self._active(self, is_active)

    def config(self, *args: Any, **kwargs: Any) -> Any:
        return self._config(self, *args, **kwargs)
