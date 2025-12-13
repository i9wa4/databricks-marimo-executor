"""Execute marimo notebooks on Databricks clusters."""

from ._version import __version__
from .executor import MarimoExecutor

__all__ = ["__version__", "MarimoExecutor"]
