# CONTRIBUTING

## 1. Development Environment Setup

### 1.1. Prerequisites

- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/)
- [mise](https://mise.jdx.dev/) (optional)
- Access to a Databricks workspace

### 1.2. Clone Repository and Install Dependencies

```bash
git clone https://github.com/i9wa4/databricks-marimo-executor.git
cd databricks-marimo-executor
uv sync
```

## 2. Databricks Configuration

### 2.1. Authentication with Databricks CLI

```bash
databricks auth login --configure-cluster
```

This saves credentials and cluster ID to `~/.databrickscfg`.

### 2.2. Configuration via Environment Variables (Alternative)

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
export DATABRICKS_CLUSTER_ID="your-cluster-id"
```

## 3. Verification

### 3.1. Install jupyter-databricks-kernel

```bash
uv run python -m jupyter_databricks_kernel.install
```

### 3.2. Start marimo

```bash
uv run marimo edit
```

The marimo editor opens in your browser.
Create a new notebook and verify that code executes on the Databricks cluster.

### 3.3. Run Tests

```bash
uv run pytest
```

## 4. Coding Standards

### 4.1. Run pre-commit

Always run pre-commit before committing.

```bash
mise exec -- pre-commit run --all-files
```

or

```bash
uv run pre-commit run --all-files
```

### 4.2. Linter and Formatter

- ruff (lint, format)
- mypy (type check)
- rumdl (markdown lint)
