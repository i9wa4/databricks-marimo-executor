"""Tests for MarimoExecutor."""

from __future__ import annotations

import pytest

from marimo_databricks import MarimoExecutor


class TestMarimoExecutor:
    """Tests for MarimoExecutor class."""

    def test_init_without_base(self) -> None:
        """Test initialization without base executor."""
        executor = MarimoExecutor()
        assert executor.base is None

    def test_execute_cell_not_implemented(self) -> None:
        """Test that execute_cell raises NotImplementedError without base."""
        executor = MarimoExecutor()

        with pytest.raises(NotImplementedError):
            executor.execute_cell(None, {}, None)  # type: ignore[arg-type]
