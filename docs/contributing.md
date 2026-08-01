# Contributing

Contributions to `mockro` are welcome. The project is a small Python package
that uses `uv` for dependency management.

## Development setup

Clone the repository and install the dev dependencies:

```bash
git clone https://github.com/dluman/mockro.git
cd mockro
uv sync
```

## Run tests

```bash
uv run pytest
```

## Lint and type check

```bash
uv run ruff check .
uv run mypy src
```

## Build the docs locally

```bash
uv run mkdocs serve
```

Open the URL shown in the terminal (usually `http://127.0.0.1:8000`) and the
docs will reload automatically when you edit files.

To verify the docs build cleanly:

```bash
uv run mkdocs build --strict
```

## Adding a new mock module

1. Add a new file under `src/mockro/` with the MicroPython module name.
2. Use `mockro.mock_function` and `mockro.mock_class` for methods and classes.
3. Add the module to the public module lists in `src/mockro/_core.py`.
4. Add a stub file under `src/mockro/stubs/` if you want editor support.
5. Add a smoke test and update the [Mocked modules](reference/modules.md) page.

## Reporting issues

Please use the [GitHub issue tracker](https://github.com/dluman/mockro/issues).
