"""Tests for the public package API."""

import tomllib
from pathlib import Path


def test_version() -> None:
    pyproject_data = tomllib.loads(Path("pyproject.toml").read_text())
    assert pyproject_data["project"]["version"] == "3.0.0"


def test_core_dependency_floor() -> None:
    pyproject_data = tomllib.loads(Path("pyproject.toml").read_text())
    assert (
        "python-getpaid-core>=3.0.0"
        in pyproject_data["project"]["dependencies"]
    )


def test_extras_defined() -> None:
    """All expected extras are listed in pyproject.toml."""
    pyproject_data = tomllib.loads(Path("pyproject.toml").read_text())
    extras = pyproject_data["project"]["optional-dependencies"]
    expected = {"payu", "paynow", "przelewy24", "bitpay", "django", "fastapi", "litestar", "backends", "frameworks", "all"}
    assert set(extras.keys()) == expected
