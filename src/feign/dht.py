"""Mock implementation of the MicroPython ``dht`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function


@mock_class("dht.DHT11")
class DHT11:
    """Mock DHT11 temperature/humidity sensor."""

    _init = mock_function("dht.DHT11.__init__", default_return=None)
    _measure = mock_function("dht.DHT11.measure", default_return=None)
    _temperature = mock_function("dht.DHT11.temperature", default_return=22.0)
    _humidity = mock_function("dht.DHT11.humidity", default_return=50.0)

    def __init__(self, pin: Any) -> None:
        self._init(self, pin)

    def measure(self) -> None:
        self._measure(self)

    def temperature(self) -> float:
        return self._temperature(self)

    def humidity(self) -> float:
        return self._humidity(self)


@mock_class("dht.DHT22")
class DHT22(DHT11):
    """Mock DHT22 temperature/humidity sensor."""
