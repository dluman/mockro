"""Mock implementation of the MicroPython ``micropython`` module."""

from __future__ import annotations

from typing import Any

from feign._factory import mock_function


def const(value: Any) -> Any:
    """Mock ``micropython.const``."""
    return value


opt_level = mock_function("micropython.opt_level", default_return=0)
mem_info = mock_function("micropython.mem_info", default_return=None)
qstr_info = mock_function("micropython.qstr_info", default_return=None)
stack_use = mock_function("micropython.stack_use", default_return=0)
heap_lock = mock_function("micropython.heap_lock", default_return=None)
heap_unlock = mock_function("micropython.heap_unlock", default_return=None)
kbd_intr = mock_function("micropython.kbd_intr", default_return=None)
schedule = mock_function("micropython.schedule", default_return=None)
repl_info = mock_function("micropython.repl_info", default_return=None)

native = mock_function("micropython.native", default_return=lambda f: f)
viper = mock_function("micropython.viper", default_return=lambda f: f)
asm_thumb = mock_function("micropython.asm_thumb", default_return=lambda f: f)
asm_xtensa = mock_function("micropython.asm_xtensa", default_return=lambda f: f)
asm_rv32imc = mock_function("micropython.asm_rv32imc", default_return=lambda f: f)
