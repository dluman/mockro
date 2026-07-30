"""Mock implementation of the MicroPython ``machine`` module."""

from __future__ import annotations

from typing import Any

from mockro._factory import mock_class, mock_function

# --- Constants ----------------------------------------------------------------

PWRON_RESET = 1
HARD_RESET = 2
WDT_RESET = 3
SOFT_RESET = 4
DEEPSLEEP_RESET = 5

IDLE = 0
SLEEP = 1
DEEPSLEEP = 2

Pin_IN = 0
Pin_OUT = 1
Pin_OPEN_DRAIN = 2
Pin_PULL_UP = 4
Pin_PULL_DOWN = 8
Pin_DRIVE_0 = 16
Pin_DRIVE_1 = 17
Pin_DRIVE_2 = 18
Pin_DRIVE_3 = 19
Pin_IRQ_FALLING = 32
Pin_IRQ_RISING = 64
Pin_IRQ_LOW_LEVEL = 128
Pin_IRQ_HIGH_LEVEL = 256

# --- Functions ----------------------------------------------------------------

reset = mock_function("machine.reset", default_return=None)
soft_reset = mock_function("machine.soft_reset", default_return=None)
unique_id = mock_function("machine.unique_id", default_return=lambda: b"\x00" * 12)
freq = mock_function("machine.freq", default_return=160_000_000)
idle = mock_function("machine.idle", default_return=None)
sleep = mock_function("machine.sleep", default_return=None)
deepsleep = mock_function("machine.deepsleep", default_return=None)
disable_irq = mock_function("machine.disable_irq", default_return=0)
enable_irq = mock_function("machine.enable_irq", default_return=None)

time_pulse_us = mock_function("machine.time_pulse_us", default_return=0)

dht_readinto = mock_function("machine.dht_readinto", default_return=None)
# --- Classes ------------------------------------------------------------------


@mock_class("machine.Pin")
class Pin:
    """Mock digital pin."""

    IN = Pin_IN
    OUT = Pin_OUT
    OPEN_DRAIN = Pin_OPEN_DRAIN
    PULL_UP = Pin_PULL_UP
    PULL_DOWN = Pin_PULL_DOWN
    DRIVE_0 = Pin_DRIVE_0
    DRIVE_1 = Pin_DRIVE_1
    DRIVE_2 = Pin_DRIVE_2
    DRIVE_3 = Pin_DRIVE_3
    IRQ_FALLING = Pin_IRQ_FALLING
    IRQ_RISING = Pin_IRQ_RISING
    IRQ_LOW_LEVEL = Pin_IRQ_LOW_LEVEL
    IRQ_HIGH_LEVEL = Pin_IRQ_HIGH_LEVEL

    _init = mock_function("machine.Pin.__init__", default_return=None)
    _value = mock_function("machine.Pin.value", default_return=0)
    _on = mock_function("machine.Pin.on", default_return=None)
    _off = mock_function("machine.Pin.off", default_return=None)
    _toggle = mock_function("machine.Pin.toggle", default_return=None)
    _irq = mock_function("machine.Pin.irq", default_return=None)
    _mode = mock_function("machine.Pin.mode", default_return=IN)
    _pull = mock_function("machine.Pin.pull", default_return=None)
    _drive = mock_function("machine.Pin.drive", default_return=DRIVE_0)
    _init = mock_function("machine.Pin.init", default_return=None)
    _deinit = mock_function("machine.Pin.deinit", default_return=None)

    def __init__(
        self,
        id: Any,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int = 0,
        alt: int = -1,
    ) -> None:
        self._init(self, id, mode, pull, value=value, drive=drive, alt=alt)

    def value(self, x: Any = None) -> Any:
        return self._value(self, x)

    def on(self) -> None:
        self._on(self)

    def off(self) -> None:
        self._off(self)

    def toggle(self) -> None:
        self._toggle(self)

    def irq(self, handler: Any = None, trigger: int = 0, *, hard: bool = False) -> Any:
        return self._irq(self, handler, trigger, hard=hard)

    def mode(self, mode: Any = None) -> Any:
        return self._mode(self, mode)

    def pull(self, pull: Any = None) -> Any:
        return self._pull(self, pull)

    def drive(self, drive: Any = None) -> Any:
        return self._drive(self, drive)

    def init(
        self,
        mode: int = -1,
        pull: int = -1,
        *,
        value: Any = None,
        drive: int = 0,
        alt: int = -1,
    ) -> None:
        self._init(self, mode, pull, value=value, drive=drive, alt=alt)

    def deinit(self) -> None:
        self._deinit(self)

    def __call__(self, x: Any = None) -> Any:
        return self.value(x)


@mock_class("machine.Signal")
class Signal:
    """Mock logical signal."""

    _init = mock_function("machine.Signal.__init__", default_return=None)
    _value = mock_function("machine.Signal.value", default_return=0)
    _on = mock_function("machine.Signal.on", default_return=None)
    _off = mock_function("machine.Signal.off", default_return=None)

    def __init__(
        self,
        pin_obj: Any,
        invert: bool = False,
        *,
        pin: Any = None,
    ) -> None:
        self._init(self, pin_obj, invert, pin=pin)

    def value(self, x: Any = None) -> Any:
        return self._value(self, x)

    def on(self) -> None:
        self._on(self)

    def off(self) -> None:
        self._off(self)


@mock_class("machine.ADC")
class ADC:
    """Mock analog-to-digital converter."""

    WIDTH_9BIT = 0
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    ATTN_0DB = 0
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    ATTN_11DB = 3

    _init = mock_function("machine.ADC.__init__", default_return=None)
    _read = mock_function("machine.ADC.read", default_return=0)
    _read_u16 = mock_function("machine.ADC.read_u16", default_return=0)
    _read_uv = mock_function("machine.ADC.read_uv", default_return=0)
    _atten = mock_function("machine.ADC.atten", default_return=None)
    _width = mock_function("machine.ADC.width", default_return=None)
    _block = mock_function("machine.ADC.block", default_return=None)

    def __init__(self, pin: Any, *, atten: int = ATTN_0DB, width: int = WIDTH_12BIT) -> None:
        self._init(self, pin, atten=atten, width=width)

    def read(self) -> int:
        return self._read(self)

    def read_u16(self) -> int:
        return self._read_u16(self)

    def read_uv(self) -> int:
        return self._read_uv(self)

    def atten(self, attenuation: Any = None) -> Any:
        return self._atten(self, attenuation)

    def width(self, width: Any = None) -> Any:
        return self._width(self, width)

    def block(self) -> Any:
        return self._block(self)


@mock_class("machine.PWM")
class PWM:
    """Mock pulse-width modulation controller."""

    _init = mock_function("machine.PWM.__init__", default_return=None)
    _deinit = mock_function("machine.PWM.deinit", default_return=None)
    _freq = mock_function("machine.PWM.freq", default_return=1000)
    _duty = mock_function("machine.PWM.duty", default_return=0)
    _duty_u16 = mock_function("machine.PWM.duty_u16", default_return=0)
    _duty_ns = mock_function("machine.PWM.duty_ns", default_return=0)

    def __init__(
        self, dest: Any, *, freq: int = 1000, duty: int = 0, duty_u16: int = 0, duty_ns: int = 0
    ) -> None:  # noqa: E501
        self._init(self, dest, freq=freq, duty=duty, duty_u16=duty_u16, duty_ns=duty_ns)

    def deinit(self) -> None:
        self._deinit(self)

    def freq(self, value: Any = None) -> Any:
        return self._freq(self, value)

    def duty(self, value: Any = None) -> Any:
        return self._duty(self, value)

    def duty_u16(self, value: Any = None) -> Any:
        return self._duty_u16(self, value)

    def duty_ns(self, value: Any = None) -> Any:
        return self._duty_ns(self, value)


@mock_class("machine.I2C")
class I2C:
    """Mock I2C bus controller."""

    _init = mock_function("machine.I2C.__init__", default_return=None)
    _scan = mock_function("machine.I2C.scan", default_return=list)
    _readfrom = mock_function(
        "machine.I2C.readfrom", default_return=lambda self, addr, nbytes, *a, **k: b"\x00" * nbytes
    )  # noqa: E501
    _readfrom_mem = mock_function(
        "machine.I2C.readfrom_mem",
        default_return=lambda self, addr, memaddr, nbytes, *a, **k: b"\x00" * nbytes,
    )  # noqa: E501
    _writeto = mock_function("machine.I2C.writeto", default_return=0)
    _writeto_mem = mock_function("machine.I2C.writeto_mem", default_return=None)
    _readfrom_mem_into = mock_function("machine.I2C.readfrom_mem_into", default_return=None)
    _writevto = mock_function("machine.I2C.writevto", default_return=0)

    def __init__(
        self,
        id: Any,
        *,
        scl: Any = None,
        sda: Any = None,
        freq: int = 400_000,
        timeout: int = 0,
    ) -> None:
        self._init(self, id, scl=scl, sda=sda, freq=freq, timeout=timeout)

    def scan(self) -> list[Any]:
        return self._scan(self)

    def readfrom(self, addr: int, nbytes: int, stop: bool = True) -> bytes:
        return self._readfrom(self, addr, nbytes, stop)

    def readfrom_into(self, addr: int, buf: bytearray, stop: bool = True) -> None:
        self._readfrom(self, addr, len(buf), stop)

    def writeto(self, addr: int, buf: bytes, stop: bool = True) -> int:
        return self._writeto(self, addr, buf, stop)

    def writevto(self, addr: int, vector: Any, stop: bool = True) -> int:
        return self._writevto(self, addr, vector, stop)

    def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, *, addrsize: int = 8) -> bytes:
        return self._readfrom_mem(self, addr, memaddr, nbytes, addrsize=addrsize)

    def readfrom_mem_into(
        self,
        addr: int,
        memaddr: int,
        buf: bytearray,
        *,
        addrsize: int = 8,
    ) -> None:
        self._readfrom_mem_into(self, addr, memaddr, buf, addrsize=addrsize)

    def writeto_mem(self, addr: int, memaddr: int, buf: bytes, *, addrsize: int = 8) -> None:
        self._writeto_mem(self, addr, memaddr, buf, addrsize=addrsize)


@mock_class("machine.SoftI2C")
class SoftI2C(I2C):
    """Mock software I2C bus."""


@mock_class("machine.SPI")
class SPI:
    """Mock SPI bus controller."""

    MSB = 0
    LSB = 1

    _init = mock_function("machine.SPI.__init__", default_return=None)
    _deinit = mock_function("machine.SPI.deinit", default_return=None)
    _read = mock_function(
        "machine.SPI.read", default_return=lambda self, nbytes, *a, **k: b"\x00" * nbytes
    )  # noqa: E501
    _readinto = mock_function("machine.SPI.readinto", default_return=None)
    _write = mock_function("machine.SPI.write", default_return=None)
    _write_readinto = mock_function("machine.SPI.write_readinto", default_return=None)

    def __init__(
        self,
        id: Any,
        *,
        baudrate: int = 500_000,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        sck: Any = None,
        mosi: Any = None,
        miso: Any = None,
        firstbit: int = MSB,
        cs: Any = None,
    ) -> None:
        self._init(
            self,
            id,
            baudrate=baudrate,
            polarity=polarity,
            phase=phase,
            bits=bits,
            sck=sck,
            mosi=mosi,
            miso=miso,
            firstbit=firstbit,
            cs=cs,
        )

    def deinit(self) -> None:
        self._deinit(self)

    def init(
        self,
        *,
        baudrate: int = 500_000,
        polarity: int = 0,
        phase: int = 0,
        bits: int = 8,
        firstbit: int = MSB,
    ) -> None:  # noqa: E501
        self._init(
            self, baudrate=baudrate, polarity=polarity, phase=phase, bits=bits, firstbit=firstbit
        )

    def read(self, nbytes: int, write: int = 0x00) -> bytes:
        return self._read(self, nbytes, write)

    def readinto(self, buf: bytearray, write: int = 0x00) -> None:
        self._readinto(self, buf, write)

    def write(self, buf: bytes) -> None:
        self._write(self, buf)

    def write_readinto(self, write_buf: bytes, read_buf: bytearray) -> None:
        self._write_readinto(self, write_buf, read_buf)


@mock_class("machine.SoftSPI")
class SoftSPI(SPI):
    """Mock software SPI bus."""


@mock_class("machine.UART")
class UART:
    """Mock UART controller."""

    _init = mock_function("machine.UART.__init__", default_return=None)
    _deinit = mock_function("machine.UART.deinit", default_return=None)
    _any = mock_function("machine.UART.any", default_return=0)
    _read = mock_function("machine.UART.read", default_return=lambda self, nbytes: b"\x00" * nbytes)
    _readinto = mock_function("machine.UART.readinto", default_return=None)
    _readline = mock_function("machine.UART.readline", default_return=b"")
    _write = mock_function("machine.UART.write", default_return=0)
    _sendbreak = mock_function("machine.UART.sendbreak", default_return=None)
    _irq = mock_function("machine.UART.irq", default_return=None)

    def __init__(
        self,
        id: Any,
        baudrate: int = 115_200,
        bits: int = 8,
        parity: Any = None,
        stop: int = 1,
        *,
        tx: Any = None,
        rx: Any = None,
        rts: Any = None,
        cts: Any = None,
        txbuf: Any = None,
        rxbuf: Any = None,
        timeout: int = 0,
        timeout_char: int = 0,
        invert: Any = None,
        flow: Any = None,
    ) -> None:
        self._init(
            self,
            id,
            baudrate,
            bits,
            parity,
            stop,
            tx=tx,
            rx=rx,
            rts=rts,
            cts=cts,
            txbuf=txbuf,
            rxbuf=rxbuf,
            timeout=timeout,
            timeout_char=timeout_char,
            invert=invert,
            flow=flow,
        )

    def deinit(self) -> None:
        self._deinit(self)

    def any(self) -> int:
        return self._any(self)

    def read(self, nbytes: Any = None) -> bytes:
        return self._read(self, nbytes)

    def readinto(self, buf: bytearray, nbytes: Any = None) -> Any:
        return self._readinto(self, buf, nbytes)

    def readline(self) -> bytes:
        return self._readline(self)

    def write(self, buf: bytes) -> int:
        return self._write(self, buf)

    def sendbreak(self) -> None:
        self._sendbreak(self)

    def irq(self, handler: Any = None, trigger: Any = 0, hard: bool = False) -> Any:
        return self._irq(self, handler, trigger, hard=hard)


@mock_class("machine.Timer")
class Timer:
    """Mock hardware timer."""

    ONE_SHOT = 0
    PERIODIC = 1

    _init = mock_function("machine.Timer.__init__", default_return=None)
    _deinit = mock_function("machine.Timer.deinit", default_return=None)
    _init_periodic = mock_function("machine.Timer.init", default_return=None)

    def __init__(
        self,
        id: Any = -1,
        *,
        mode: int = PERIODIC,
        callback: Any = None,
        freq: Any = None,
        period: Any = None,
    ) -> None:  # noqa: E501
        self._init(self, id, mode=mode, callback=callback, freq=freq, period=period)

    def init(
        self, *, mode: int = PERIODIC, callback: Any = None, freq: Any = None, period: Any = None
    ) -> None:  # noqa: E501
        self._init_periodic(self, mode=mode, callback=callback, freq=freq, period=period)

    def deinit(self) -> None:
        self._deinit(self)


@mock_class("machine.RTC")
class RTC:
    """Mock real-time clock."""

    _init = mock_function("machine.RTC.__init__", default_return=None)
    _datetime = mock_function(
        "machine.RTC.datetime", default_return=lambda: (2020, 1, 1, 0, 0, 0, 0, 0)
    )

    def __init__(self, id: Any = 0) -> None:
        self._init(self, id)

    def datetime(self, datetimetuple: Any = None) -> Any:
        return self._datetime(self, datetimetuple)


@mock_class("machine.WDT")
class WDT:
    """Mock watchdog timer."""

    _init = mock_function("machine.WDT.__init__", default_return=None)
    _feed = mock_function("machine.WDT.feed", default_return=None)

    def __init__(self, id: int = 0, timeout: int = 5000) -> None:
        self._init(self, id, timeout)

    def feed(self) -> None:
        self._feed(self)


@mock_class("machine.TouchPad")
class TouchPad:
    """Mock ESP32 touch pad."""

    _init = mock_function("machine.TouchPad.__init__", default_return=None)
    _read = mock_function("machine.TouchPad.read", default_return=0)
    _config = mock_function("machine.TouchPad.config", default_return=None)

    def __init__(self, pin: Any) -> None:
        self._init(self, pin)

    def read(self) -> int:
        return self._read(self)

    def config(self, value: Any = None) -> Any:
        return self._config(self, value)


def __getattr__(name: str) -> Any:
    """Lazy fallback for less common machine members."""
    if name == "mem8":
        return mock_function("machine.mem8", default_return=0)
    if name == "mem16":
        return mock_function("machine.mem16", default_return=0)
    if name == "mem32":
        return mock_function("machine.mem32", default_return=0)
    raise AttributeError(f"module 'machine' has no attribute '{name}'")
