"""Tests for MarimoExecutor."""

from __future__ import annotations

from databricks_marimo_executor import MarimoExecutor


class TestMarimoExecutor:
    """Tests for MarimoExecutor class."""

    def test_init_without_base(self) -> None:
        """Test initialization without base executor."""
        executor = MarimoExecutor()
        assert executor.base is None
        assert executor._databricks_executor is None
        assert executor._config is None

    def test_init_with_base(self) -> None:
        """Test initialization with base executor."""

        class MockExecutor:
            pass

        mock_base = MockExecutor()
        executor = MarimoExecutor(base=mock_base)  # type: ignore[arg-type]
        assert executor.base is mock_base
