"""Sphinx configuration for python-getpaid."""

project = "python-getpaid"
author = "Dominik Kozaczko"
project_copyright = "2022-2026, Dominik Kozaczko"

extensions = [
    "sphinx.ext.intersphinx",
    "myst_parser",
]

html_theme = "furo"
html_title = "python-getpaid"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
