# CLI scaffold

`mockro` includes a small CLI for scaffolding new projects that are already
set up for local development and testing.

## Create a new project

```bash
mockro init my_project
```

This creates a project with:

```
my_project/
├── pyproject.toml
├── README.md
├── src/
│   └── main.py
├── tests/
│   ├── conftest.py
│   └── test_main.py
└── stubs/
    └── machine.pyi
```

- `pyproject.toml` — project metadata with `mockro` and `pytest` as dev dependencies.
- `src/main.py` — a starter MicroPython script.
- `tests/conftest.py` — example overrides.
- `tests/test_main.py` — starter tests.
- `stubs/` — `.pyi` type stubs so editors understand the mocked MicroPython APIs.

## Run the scaffolded project

```bash
cd my_project
uv run python src/main.py
```

## Run tests

```bash
cd my_project
uv run pytest
```

## Customize the scaffold

After scaffolding, edit the files to match your project:

1. Rename `my_project` in `pyproject.toml` and `README.md` if needed.
2. Replace the starter code in `src/main.py` with your firmware.
3. Uncomment and adjust the example patches in `tests/conftest.py`.
4. Add more tests to `tests/test_main.py` or create new test files.

## Example workflow

```bash
# Create a new project
mockro init weather_station

# Move into it and run the starter code
cd weather_station
uv run python src/main.py

# Verify tests pass
uv run pytest
```

!!! note

    The scaffold uses `uv` and `dependency-groups` for dependency management. If
    you prefer plain `pip` and `requirements.txt`, replace the dependency
    section in `pyproject.toml` accordingly.
