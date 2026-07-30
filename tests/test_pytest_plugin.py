"""Tests for the pytest plugin behavior."""

from __future__ import annotations

import sys

import feign


def test_pytest_plugin_activates_mocks() -> None:
    # When this test file is collected by pytest, the plugin has already run.
    assert "machine" in sys.modules
    assert "network" in sys.modules


def test_conftest_overrides_persist_across_tests() -> None:
    # This checks that the autouse fixture does not wipe conftest overrides.
    # We set an override here and it should remain set unless the fixture
    # snapshots and restores around tests, which would undo it.
    feign.patch("machine.Pin.value", return_value=42)
    import machine

    pin = machine.Pin(2, machine.Pin.IN)
    assert pin.value() == 42


def test_previous_test_override_is_restored() -> None:
    import machine

    pin = machine.Pin(2, machine.Pin.IN)
    # The override from the previous test should have been restored to default.
    assert pin.value() == 0


def test_recorder_does_not_leak_between_tests() -> None:
    feign.get_recorder().clear()
    import machine

    pin = machine.Pin(2, machine.Pin.IN)
    pin.value()
    assert len(feign.get_recorder().calls("machine.Pin.value")) == 1


def test_recorder_was_cleared_after_previous_test() -> None:
    assert len(feign.get_recorder().calls("machine.Pin.value")) == 0
