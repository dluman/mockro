"""Project scaffolding for ``feign init``."""

from __future__ import annotations

from importlib import resources
from pathlib import Path

from feign import __version__

_PROJECT_TEMPLATES: dict[str, str] = {
    "pyproject.toml": """[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{name}"
version = "0.1.0"
description = "MicroPython assignment project with feign mocks."
readme = "README.md"
requires-python = ">=3.11"
license = {{ text = "MIT" }}

[dependency-groups]
dev = [
    "feign>={feign_version}",
    "pytest>=8",
]

[tool.hatch.build.targets.wheel]
bypass-selection = true

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.mypy]
mypy_path = ["stubs"]
""",
    "README.md": """# {name}

This assignment is designed to be developed and tested on a normal computer
using [feign](https://github.com/dougluman/feign), which mocks MicroPython
libraries such as ``machine`` and ``network``.

## Run the code with mocks

```bash
uv run python src/main.py
```

You can also use the explicit wrapper:

```bash
uv run feign run src/main.py
```

## Run tests

```bash
uv run pytest
```

## Override mock behavior

Edit ``tests/conftest.py`` to change how the mocked hardware behaves for tests.
""",
    "src/main.py": """import machine
import network


def main() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)


if __name__ == "__main__":
    main()
""",
    "tests/conftest.py": """import feign

# Example overrides for the assignment.  Uncomment and adjust as needed.
# feign.patch("machine.Pin.value", return_value=1)
# feign.patch("network.WLAN.isconnected", return_value=True)
""",
    "tests/test_main.py": """import machine
import network


def test_led_can_be_turned_on() -> None:
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()
    assert led.value() == 0  # change once overrides are configured


def test_wlan_initially_inactive() -> None:
    wlan = network.WLAN(network.STA_IF)
    assert not wlan.active()
""",
    ".gitignore": """__pycache__/
*.pyc
*.pyo
.env
.venv/
venv/
dist/
build/
*.egg-info/
""",
}


def init_project(target: Path) -> None:
    """Create a new feign-enabled project at ``target``."""
    if target.exists():
        raise FileExistsError(f"Project directory already exists: {target}")

    target.mkdir(parents=True)
    (target / "src").mkdir()
    (target / "tests").mkdir()

    context = {
        "name": target.name,
        "feign_version": __version__,
    }

    for relative_path, template in _PROJECT_TEMPLATES.items():
        path = target / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(template.format(**context), encoding="utf-8")

    stubs_dir = target / "stubs"
    stubs_dir.mkdir(exist_ok=True)
    stubs_source = resources.files("feign") / "stubs"
    for stub_path in stubs_source.iterdir():
        if stub_path.is_file() and stub_path.name.endswith(".pyi"):
            target_stub = stubs_dir / stub_path.name
            target_stub.write_text(stub_path.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Created feign-enabled project: {target}")
