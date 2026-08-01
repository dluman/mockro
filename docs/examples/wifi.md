# Wi-Fi connection

`network.WLAN` lets firmware connect to Wi-Fi. With `mockro`, you can test
connection logic without an access point.

## Firmware code

```python title="src/wifi.py"
import network
import utime


class WiFi:
    def __init__(self) -> None:
        self._wlan = network.WLAN(network.STA_IF)

    def connect(self, ssid: str, password: str, timeout_ms: int = 10000) -> bool:
        self._wlan.active(True)
        self._wlan.connect(ssid, password)

        deadline = utime.ticks_ms() + timeout_ms
        while not self._wlan.isconnected():
            if utime.ticks_ms() > deadline:
                return False
            utime.sleep_ms(100)
        return True

    def is_connected(self) -> bool:
        return self._wlan.isconnected()
```

## Test successful connection

Patch `isconnected` to return `True`:

```python title="tests/conftest.py"
import mockro

mockro.patch("network.WLAN.isconnected", return_value=True)
```

```python title="tests/test_wifi.py"
from wifi import WiFi


def test_connect_succeeds() -> None:
    wifi = WiFi()
    assert wifi.connect("my-ssid", "my-password")
    assert wifi.is_connected()
```

## Test timeout

Simulate a connection that never succeeds:

```python title="tests/test_wifi.py"
import mockro
from wifi import WiFi


def test_connect_times_out() -> None:
    mockro.patch("network.WLAN.isconnected", return_value=False)
    mockro.patch("utime.ticks_ms", side_effect=[0, 100, 10000, 10001])
    mockro.patch("utime.sleep_ms", return_value=None)

    wifi = WiFi()
    assert not wifi.connect("my-ssid", "my-password")
```

## Verify connection arguments

```python title="tests/test_wifi.py"
import mockro
from wifi import WiFi


def test_connect_activates_interface() -> None:
    wifi = WiFi()
    wifi.connect("my-ssid", "my-password")

    active_calls = mockro.get_recorder().calls("network.WLAN.active")
    assert len(active_calls) == 1
    assert active_calls[0][0][1] is True

    connect_calls = mockro.get_recorder().calls("network.WLAN.connect")
    assert len(connect_calls) == 1
    assert connect_calls[0][0][1] == "my-ssid"
    assert connect_calls[0][0][2] == "my-password"
```

!!! tip

    Override `utime.ticks_ms` and `utime.sleep_ms` to make timeout loops fast
    and deterministic in tests.
