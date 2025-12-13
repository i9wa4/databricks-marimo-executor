"""Marimo Executor for Databricks remote execution."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from jupyter_databricks_kernel.config import Config
from jupyter_databricks_kernel.executor import DatabricksExecutor

if TYPE_CHECKING:
    from marimo._ast.cell import CellImpl
    from marimo._runtime.dataflow import DirectedGraph
    from marimo._runtime.executor import Executor

logger = logging.getLogger(__name__)


class MarimoExecutor:
    """Marimo Executor that runs cells on Databricks clusters.

    This executor is registered as a marimo entry point and intercepts
    cell execution to run code remotely on Databricks.
    """

    def __init__(self, base: Executor | None = None) -> None:
        self.base = base
        self._databricks_executor: DatabricksExecutor | None = None
        self._config: Config | None = None

    def _ensure_databricks_executor(self) -> DatabricksExecutor:
        """Ensure the DatabricksExecutor is initialized."""
        if self._databricks_executor is None:
            self._config = Config.load()
            errors = self._config.validate()
            if errors:
                raise RuntimeError(f"Databricks configuration error: {errors}")
            self._databricks_executor = DatabricksExecutor(self._config)
        return self._databricks_executor

    def execute_cell(
        self,
        cell: CellImpl,
        glbls: dict[str, Any],
        graph: DirectedGraph,
    ) -> Any:
        """Execute a cell on Databricks.

        Args:
            cell: The cell to execute.
            glbls: Global variables dictionary.
            graph: The dataflow graph.

        Returns:
            The result of the cell execution.
        """
        try:
            executor = self._ensure_databricks_executor()
            result = executor.execute(cell.code)

            if result.status == "error":
                error_msg = result.error or "Unknown error"
                if result.traceback:
                    error_msg += "\n" + "\n".join(result.traceback)
                raise RuntimeError(error_msg)

            # Return the output if available
            if result.output:
                return result.output
            return None

        except Exception as e:
            logger.warning("Databricks execution failed: %s, falling back", e)
            # Fall back to base executor
            if self.base is not None:
                return self.base.execute_cell(cell, glbls, graph)
            raise

    async def execute_cell_async(
        self,
        cell: CellImpl,
        glbls: dict[str, Any],
        graph: DirectedGraph,
    ) -> Any:
        """Execute a cell asynchronously on Databricks.

        Note: Currently uses synchronous execution internally.

        Args:
            cell: The cell to execute.
            glbls: Global variables dictionary.
            graph: The dataflow graph.

        Returns:
            The result of the cell execution.
        """
        # For now, just call the sync version
        # TODO: Implement true async execution
        return self.execute_cell(cell, glbls, graph)
