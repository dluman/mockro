"""Smoke tests for core mockro functionality."""

from __future__ import annotations

import sys

import mockro


def test_activate_installs_modules() -> None:
    mockro.activate()
    assert "machine" in sys.modules
    assert "network" in sys.modules


def test_import_machine() -> None:
    mockro.activate()
    import machine
    import network

    assert machine.Pin.IN == 0
    assert network.STA_IF == 0


def test_default_pin_value() -> None:
    mockro.activate()
    import machine

    pin = machine.Pin(2, machine.Pin.IN)
    assert pin.value() == 0


def test_patch_return_value() -> None:
    mockro.activate()
    import machine

    mockro.patch("machine.Pin.value", return_value=1)
    pin = machine.Pin(2, machine.Pin.IN)
    assert pin.value() == 1


def test_patch_side_effect() -> None:
    mockro.activate()
    import machine

    mockro.patch("machine.Pin.value", side_effect=[1, 0, 1])
    pin = machine.Pin(2, machine.Pin.IN)
    assert pin.value() == 1
    assert pin.value() == 0
    assert pin.value() == 1


def test_override_context_manager() -> None:
    mockro.activate()
    import machine

    with mockro.override(machine_Pin_value=1):
        pin = machine.Pin(2, machine.Pin.IN)
        assert pin.value() == 1

    assert pin.value() == 0


def test_recorder_records_calls() -> None:
    mockro.get_recorder().clear()
    mockro.activate()
    import machine

    pin = machine.Pin(2, machine.Pin.IN)
    pin.value()
    calls = mockro.get_recorder().calls("machine.Pin.value")
    assert len(calls) == 1


def test_class_override() -> None:
    class CustomPin:
        def __init__(self, *args: object, **kwargs: object) -> None:
            pass

        def value(self) -> int:
            return 42

    mockro.activate()
    mockro.patch("machine.Pin", CustomPin)
    import machine

    pin = machine.Pin(2)
    assert pin.value() == 42


def test_freq_default() -> None:
    mockro.activate()
    import machine

    assert machine.freq() == 160_000_000


def test_network_wlan_isconnected() -> None:
    mockro.activate()
    import network

    mockro.patch("network.WLAN.isconnected", return_value=True)
    wlan = network.WLAN(network.STA_IF)
    assert wlan.isconnected()


def test_socket_create() -> None:
    mockro.activate()
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()


def test_time_functions() -> None:
    mockro.activate()
    import utime

    assert utime.ticks_add(10, 5) == 15


def test_json_loads() -> None:
    mockro.activate()
    import ujson

    data = ujson.loads('{"a": 1}')
    assert data == {"a": 1}
