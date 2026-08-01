# Changelog

All notable changes to `mockro` are documented in this file.

## 0.1.0

- Initial release.
- Mocks for the MicroPython standard library and common port-specific modules.
- `mockro.activate`, `mockro.patch`, `mockro.override`, and `mockro.get_recorder`
  public API.
- pytest plugin that auto-installs mocks and isolates the registry between tests.
- CLI commands `mockro run` and `mockro init`.
- Project scaffolding with `pyproject.toml`, starter code, tests, and `.pyi` stubs.
