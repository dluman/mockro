"""Pytest plugin that auto-activates mockro mocks."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

import pytest

import mockro
from mockro._core import get_registry


def pytest_configure(config: Any) -> None:  # noqa: ANN401
    """Install mockro mocks before tests are collected."""
    mockro.activate()


@pytest.fixture(autouse=True)
def _mockro_registry_snapshot() -> Generator[None, None, None]:
    """Restore override registry after each test.

    This keeps overrides made in ``conftest.py`` or session-scoped fixtures
    intact while preventing one test's local patches from leaking into the
    next.
    """
    registry = get_registry()
    snapshot = registry.snapshot()
    mockro.get_recorder().clear()
    try:
        yield
    finally:
        registry.restore(snapshot)
