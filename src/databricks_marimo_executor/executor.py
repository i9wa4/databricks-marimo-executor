"""Marimo Executor for Databricks remote execution."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from marimo._ast.cell import CellImpl
    from marimo._runtime.dataflow import DirectedGraph
    from marimo._runtime.executor import Executor


class MarimoExecutor:
    """Marimo Executor that runs cells on Databricks clusters.

    This executor is registered as a marimo entry point and intercepts
    cell execution to run code remotely on Databricks.

    Note: This is a placeholder implementation for v0.1.0.
    Full implementation is planned for future releases.
    """

    def __init__(self, base: Executor | None = None) -> None:
        self.base = base

    def execute_cell(
        self,
        cell: CellImpl,
        glbls: dict[str, Any],
        graph: DirectedGraph,
    ) -> Any:
        """Execute a cell on Databricks.

        Note: Not yet implemented. Falls back to base executor.
        """
        if self.base is not None:
            return self.base.execute_cell(cell, glbls, graph)
        raise NotImplementedError("MarimoExecutor is not yet implemented")

    async def execute_cell_async(
        self,
        cell: CellImpl,
        glbls: dict[str, Any],
        graph: DirectedGraph,
    ) -> Any:
        """Execute a cell asynchronously on Databricks.

        Note: Not yet implemented. Falls back to base executor.
        """
        if self.base is not None:
            return await self.base.execute_cell_async(cell, glbls, graph)
        raise NotImplementedError("MarimoExecutor is not yet implemented")
