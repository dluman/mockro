"""Mock implementation of the MicroPython ``bluetooth`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function

FLAG_READ = 1
FLAG_WRITE = 2
FLAG_NOTIFY = 4
FLAG_INDICATE = 8


@mock_class("bluetooth.BLE")
class BLE:
    """Mock Bluetooth Low Energy controller."""

    _active = mock_function("bluetooth.BLE.active", default_return=False)
    _config = mock_function("bluetooth.BLE.config", default_return=None)
    _irq = mock_function("bluetooth.BLE.irq", default_return=None)
    _gap_scan = mock_function("bluetooth.BLE.gap_scan", default_return=None)
    _gap_connect = mock_function("bluetooth.BLE.gap_connect", default_return=None)
    _gap_disconnect = mock_function("bluetooth.BLE.gap_disconnect", default_return=False)
    _gatts_register_services = mock_function(
        "bluetooth.BLE.gatts_register_services", default_return=None
    )
    _gatts_read = mock_function("bluetooth.BLE.gatts_read", default_return=b"")
    _gatts_write = mock_function("bluetooth.BLE.gatts_write", default_return=None)
    _gatts_notify = mock_function("bluetooth.BLE.gatts_notify", default_return=None)
    _gatts_set_buffer = mock_function("bluetooth.BLE.gatts_set_buffer", default_return=None)
    _gattc_discover_services = mock_function(
        "bluetooth.BLE.gattc_discover_services", default_return=None
    )
    _gattc_discover_characteristics = mock_function(
        "bluetooth.BLE.gattc_discover_characteristics", default_return=None
    )
    _gattc_read = mock_function("bluetooth.BLE.gattc_read", default_return=None)
    _gattc_write = mock_function("bluetooth.BLE.gattc_write", default_return=None)
    _gap_advertise = mock_function("bluetooth.BLE.gap_advertise", default_return=None)
    _gap_pair = mock_function("bluetooth.BLE.gap_pair", default_return=None)
    _gap_passkey = mock_function("bluetooth.BLE.gap_passkey", default_return=None)

    def __init__(self) -> None:
        pass

    def active(self, active: Any = None) -> Any:
        return self._active(self, active)

    def config(self, *args: Any, **kwargs: Any) -> Any:
        return self._config(self, *args, **kwargs)

    def irq(self, handler: Any, trigger: int = 0) -> None:
        self._irq(self, handler, trigger)

    def gap_scan(
        self,
        duration_ms: int = 0,
        interval_us: int = 128_000,
        window_us: int = 11_250,
        active: bool = False,
    ) -> None:  # noqa: E501
        self._gap_scan(self, duration_ms, interval_us, window_us, active)

    def gap_connect(self, addr_type: int, addr: bytes, scan_interval_us: int = 11_250) -> None:
        self._gap_connect(self, addr_type, addr, scan_interval_us)

    def gap_disconnect(self, conn_handle: int) -> bool:
        return self._gap_disconnect(self, conn_handle)

    def gatts_register_services(self, services: Any) -> None:
        self._gatts_register_services(self, services)

    def gatts_read(self, value_handle: int) -> bytes:
        return self._gatts_read(self, value_handle)

    def gatts_write(self, value_handle: int, data: bytes = b"", send_update: bool = False) -> None:
        self._gatts_write(self, value_handle, data, send_update)

    def gatts_notify(self, conn_handle: int, value_handle: int, data: bytes | None = None) -> None:
        self._gatts_notify(self, conn_handle, value_handle, data)

    def gatts_set_buffer(self, value_handle: int, len: int, append: bool = False) -> None:
        self._gatts_set_buffer(self, value_handle, len, append)

    def gattc_discover_services(self, conn_handle: int, uuid: Any = None) -> None:
        self._gattc_discover_services(self, conn_handle, uuid)

    def gattc_discover_characteristics(
        self, conn_handle: int, start_handle: int, end_handle: int, uuid: Any = None
    ) -> None:  # noqa: E501
        self._gattc_discover_characteristics(self, conn_handle, start_handle, end_handle, uuid)

    def gattc_read(self, conn_handle: int, value_handle: int) -> None:
        self._gattc_read(self, conn_handle, value_handle)

    def gattc_write(self, conn_handle: int, value_handle: int, data: bytes, mode: int = 0) -> None:
        self._gattc_write(self, conn_handle, value_handle, data, mode)

    def gap_advertise(
        self,
        interval_us: int,
        adv_data: Any = None,
        resp_data: Any = None,
        connectable: bool = True,
    ) -> None:  # noqa: E501
        self._gap_advertise(self, interval_us, adv_data, resp_data, connectable)

    def gap_pair(self, conn_handle: int) -> None:
        self._gap_pair(self, conn_handle)

    def gap_passkey(self, conn_handle: int, action: int, key: Any) -> None:
        self._gap_passkey(self, conn_handle, action, key)


UUID = mock_function("bluetooth.UUID", default_return=lambda value: value)
