"""Tests for the command-line interface."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from feign.cli import main


def test_run_script_with_mocks(tmp_path: Path) -> None:
    script = tmp_path / "script.py"
    script.write_text(
        "import machine\nprint(machine.freq())\n",
        encoding="utf-8",
    )
    main(["run", str(script)])


def test_run_script_imports_socket_alias(tmp_path: Path) -> None:
    script = tmp_path / "script.py"
    script.write_text(
        "import socket\n"
        "s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
        "print(type(s).__module__)\n",
        encoding="utf-8",
    )
    main(["run", str(script)])


def test_init_creates_project(tmp_path: Path) -> None:
    target = tmp_path / "new_project"
    main(["init", "--path", str(tmp_path), "new_project"])
    assert (target / "pyproject.toml").exists()
    assert (target / "src" / "main.py").exists()
    assert (target / "stubs" / "machine.pyi").exists()


def test_init_refuses_existing_directory(tmp_path: Path) -> None:
    target = tmp_path / "exists"
    target.mkdir()
    with pytest.raises(FileExistsError):
        main(["init", "--path", str(tmp_path), "exists"])


def test_cli_entry_point_runs() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "feign", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "feign" in result.stdout


def test_python_m_feign_run(tmp_path: Path) -> None:
    script = tmp_path / "script.py"
    script.write_text("import machine\nprint(machine.freq())\n", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-m", "feign", "run", str(script)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "160000000" in result.stdout
