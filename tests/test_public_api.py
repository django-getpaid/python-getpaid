"""Tests for the public package API."""

import importlib.metadata
import tomllib
from pathlib import Path


def test_version() -> None:
    """The installed distribution version matches pyproject.toml."""
    pyproject_data = tomllib.loads(Path("pyproject.toml").read_text())
    assert (
        importlib.metadata.version("python-getpaid")
        == pyproject_data["project"]["version"]
    )


def test_core_dependency_floor() -> None:
    pyproject_data = tomllib.loads(Path("pyproject.toml").read_text())
    assert (
        "python-getpaid-core>=3.1.0"
        in pyproject_data["project"]["dependencies"]
    )


def test_extras_defined() -> None:
    """All expected extras are listed in pyproject.toml."""
    pyproject_data = tomllib.loads(Path("pyproject.toml").read_text())
    extras = pyproject_data["project"]["optional-dependencies"]
    expected = {"payu", "paynow", "przelewy24", "django", "backends", "frameworks", "all"}
    assert set(extras.keys()) == expected
