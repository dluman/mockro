"""Command-line interface for mockro."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import mockro
from mockro._template import init_project


def _run_script(script_path: str, script_args: list[str]) -> None:
    """Activate mocks and execute a Python script."""
    mockro.activate(aliases=True)

    script_path = os.path.abspath(script_path)
    script_dir = os.path.dirname(script_path)
    if script_dir:
        sys.path.insert(0, script_dir)

    sys.argv = [script_path, *script_args]

    with open(script_path, "rb") as f:
        code = compile(f.read(), script_path, "exec")

    namespace = {
        "__name__": "__main__",
        "__file__": script_path,
        "__cached__": None,
    }
    exec(code, namespace)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mockro",
        description=(
            "Run Python scripts with MicroPython mocks, or scaffold mockro-enabled projects."
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser(
        "run",
        help="Run a Python script with mockro mocks active",
    )
    run_parser.add_argument("script", help="Python script to run")
    run_parser.add_argument(
        "script_args",
        nargs=argparse.REMAINDER,
        help="Arguments to pass to the script",
    )

    init_parser = subparsers.add_parser(
        "init",
        help="Create a new mockro-enabled assignment project",
    )
    init_parser.add_argument("name", help="Project directory name")
    init_parser.add_argument(
        "--path",
        default=".",
        help="Parent directory for the new project (default: current directory)",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the ``mockro`` console script."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        _run_script(args.script, args.script_args)
        return 0

    if args.command == "init":
        target = Path(args.path) / args.name
        init_project(target)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
