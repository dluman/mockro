# Command-line interface

`mockro` provides a small command-line interface for running scripts with full
mock aliases and for scaffolding new projects.

## `mockro run`

Run a Python script with `mockro` mocks active, including the non-`u` aliases
such as `socket`, `time`, `os`, `json`, and `asyncio`:

```bash
mockro run main.py
python -m mockro run main.py
```

Pass additional arguments to the script after the script name:

```bash
mockro run main.py --interval 500
```

This is the easiest way to run a script that imports bare MicroPython module
names like `import socket` instead of `import usocket`.

## `mockro init`

Create a new project pre-configured for `mockro` development:

```bash
mockro init my_project
```

Create the project in a different parent directory:

```bash
mockro init my_project --path ../projects
```

The scaffold includes `pyproject.toml`, starter source, tests, and `.pyi` stubs.
See the [CLI scaffold example](examples/cli.md) for details.

## `mockro --help`

Show available commands:

```bash
mockro --help
mockro run --help
mockro init --help
```
