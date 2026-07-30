"""Mock implementation of the Raspberry Pi Pico-specific ``rp2`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_class, mock_function

PIO0 = 0
PIO1 = 1


@mock_class("rp2.PIO")
class PIO:
    """Mock RP2040 PIO controller."""

    _init = mock_function("rp2.PIO.__init__", default_return=None)
    _add_program = mock_function("rp2.PIO.add_program", default_return=None)
    _remove_program = mock_function("rp2.PIO.remove_program", default_return=None)
    _state_machine = mock_function("rp2.PIO.state_machine", default_return=None)

    def __init__(self, id: int) -> None:
        self._init(self, id)

    def add_program(self, prog: Any) -> None:
        self._add_program(self, prog)

    def remove_program(self, prog: Any = None) -> None:
        self._remove_program(self, prog)

    def state_machine(
        self,
        id: int,
        program: Any,
        *,
        freq: int = -1,
        in_base: Any = None,
        out_base: Any = None,
        set_base: Any = None,
        sideset_base: Any = None,
        jmp_pin: Any = None,
        push_thresh: int = 32,
        pull_thresh: int = 32,
    ) -> StateMachine:
        return self._state_machine(
            self,
            id,
            program,
            freq=freq,
            in_base=in_base,
            out_base=out_base,
            set_base=set_base,
            sideset_base=sideset_base,
            jmp_pin=jmp_pin,
            push_thresh=push_thresh,
            pull_thresh=pull_thresh,
        )


@mock_class("rp2.StateMachine")
class StateMachine:
    """Mock RP2040 PIO state machine."""

    _init = mock_function("rp2.StateMachine.__init__", default_return=None)
    _active = mock_function("rp2.StateMachine.active", default_return=None)
    _restart = mock_function("rp2.StateMachine.restart", default_return=None)
    _exec = mock_function("rp2.StateMachine.exec", default_return=None)
    _get = mock_function("rp2.StateMachine.get", default_return=0)
    _put = mock_function("rp2.StateMachine.put", default_return=None)
    _rx_fifo = mock_function("rp2.StateMachine.rx_fifo", default_return=0)
    _tx_fifo = mock_function("rp2.StateMachine.tx_fifo", default_return=0)
    _irq = mock_function("rp2.StateMachine.irq", default_return=None)

    def __init__(
        self,
        id: Any,
        program: Any,
        *,
        freq: int = -1,
        in_base: Any = None,
        out_base: Any = None,
        set_base: Any = None,
        sideset_base: Any = None,
        jmp_pin: Any = None,
        push_thresh: int = 32,
        pull_thresh: int = 32,
    ) -> None:
        self._init(
            self,
            id,
            program,
            freq=freq,
            in_base=in_base,
            out_base=out_base,
            set_base=set_base,
            sideset_base=sideset_base,
            jmp_pin=jmp_pin,
            push_thresh=push_thresh,
            pull_thresh=pull_thresh,
        )

    def active(self, value: Any = None) -> Any:
        return self._active(self, value)

    def restart(self) -> None:
        self._restart(self)

    def exec(self, instr: Any) -> None:
        self._exec(self, instr)

    def get(self, buf: Any = None, shift: int = 0) -> Any:
        return self._get(self, buf, shift)

    def put(self, value: Any, shift: int = 0) -> None:
        self._put(self, value, shift)

    def rx_fifo(self) -> int:
        return self._rx_fifo(self)

    def tx_fifo(self) -> int:
        return self._tx_fifo(self)

    def irq(self, handler: Any) -> Any:
        return self._irq(self, handler)


def asm_pio(**kwargs: Any) -> Any:
    """Mock PIO assembler decorator."""

    def decorator(func: Any) -> Any:
        return func

    return decorator


PIOIN = 0
PIOOUT = 1
PIOIRQ = 2

bootsel_button = mock_function("rp2.bootsel_button", default_return=False)
country = mock_function("rp2.country", default_return=lambda: "XX")


def __getattr__(name: str) -> Any:
    if name == "Flash":
        return mock_class("rp2.Flash")(type("Flash", (object,), {}))
    raise AttributeError(f"module 'rp2' has no attribute '{name}'")
