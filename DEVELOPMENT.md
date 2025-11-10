# Development Guide

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip
- git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/umitkacar/NLP_Research.git
cd NLP_Research

# Run the setup script
bash scripts/setup.sh

# Or manually:
pip install -e ".[dev]"
pre-commit install
```

## 🛠️ Development Tools

This project uses modern Python development tools:

- **[Hatch](https://hatch.pypa.io/)** - Build system and project management
- **[Ruff](https://github.com/astral-sh/ruff)** - Fast Python linter (replaces flake8, isort, etc.)
- **[Black](https://github.com/psf/black)** - Code formatter
- **[MyPy](https://mypy-lang.org/)** - Static type checker
- **[Pytest](https://pytest.org/)** - Testing framework
- **[Coverage](https://coverage.readthedocs.io/)** - Code coverage
- **[Pre-commit](https://pre-commit.com/)** - Git hooks framework

## 📝 Common Tasks

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run only unit tests
make test-unit

# Run only integration tests
make test-integration

# Run specific test file
pytest tests/test_utils.py

# Run specific test
pytest tests/test_utils.py::test_get_device
```

### Code Quality

```bash
# Lint code
make lint

# Format code
make format

# Type check
make type-check

# Run all checks
make check-all

# Run pre-commit hooks
make pre-commit
```

### Using Hatch

```bash
# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Lint code
hatch run lint:check

# Format code
hatch run lint:format

# Build package
hatch build

# Show version
hatch version

# Bump version
hatch version patch  # 0.1.0 -> 0.1.1
hatch version minor  # 0.1.0 -> 0.2.0
hatch version major  # 0.1.0 -> 1.0.0
```

### Building and Publishing

```bash
# Build distribution
make build

# Publish to Test PyPI
make publish-test

# Publish to PyPI
make publish
```

## 📂 Project Structure

```
NLP_Research/
├── src/
│   └── nlp_research/          # Main package
│       ├── __init__.py
│       ├── models.py          # NLP models
│       ├── preprocessing.py   # Text preprocessing
│       └── utils.py           # Utility functions
├── tests/                     # Test files
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures
│   ├── test_models.py
│   ├── test_preprocessing.py
│   └── test_utils.py
├── examples/                  # Example scripts
│   └── basic_usage.py
├── scripts/                   # Development scripts
│   └── setup.sh
├── docs/                      # Documentation
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI/CD
├── pyproject.toml            # Project configuration
├── .pre-commit-config.yaml   # Pre-commit hooks
├── Makefile                  # Development commands
├── README.md
└── DEVELOPMENT.md            # This file
```

## 🧪 Writing Tests

### Test Structure

- Place tests in `tests/` directory
- Name test files with `test_*.py` prefix
- Use pytest fixtures in `conftest.py`

### Test Categories

Mark tests with appropriate markers:

```python
import pytest

@pytest.mark.unit
def test_simple_function():
    """Fast unit test."""
    assert True

@pytest.mark.integration
@pytest.mark.slow
def test_model_loading():
    """Slow integration test."""
    # Test that requires model download
    pass
```

Run specific test categories:

```bash
# Run only unit tests
pytest -m unit

# Run all except slow tests
pytest -m "not slow"
```

## 🎨 Code Style

### Type Hints

Use type hints for all functions:

```python
def process_text(text: str, max_length: int = 512) -> dict[str, Any]:
    """Process text and return results."""
    return {"text": text, "length": len(text)}
```

### Docstrings

Use Google-style docstrings:

```python
def my_function(param1: str, param2: int) -> bool:
    """Short description.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param2 is negative

    Example:
        >>> my_function("test", 42)
        True
    """
    if param2 < 0:
        raise ValueError("param2 must be non-negative")
    return True
```

### Import Order

Imports are automatically sorted by Ruff:

1. Standard library imports
2. Third-party imports
3. Local imports

```python
import json
from pathlib import Path

import torch
from transformers import AutoModel

from nlp_research.utils import get_device
```

## 🔧 Configuration Files

### pyproject.toml

Main configuration file containing:
- Project metadata
- Dependencies
- Build system (Hatch)
- Tool configurations (Ruff, Black, MyPy, Pytest, Coverage)

### .pre-commit-config.yaml

Pre-commit hooks that run before each commit:
- Trailing whitespace removal
- File formatting (Black, Ruff)
- Linting (Ruff, Bandit)
- Type checking (MyPy)
- Markdown linting

### Makefile

Convenient shortcuts for common tasks. See `make help` for all commands.

## 🐛 Debugging

### Using IPython

```bash
# Start IPython with package loaded
make shell

# Or manually
ipython -i -c "from nlp_research import *"
```

### Using Jupyter

```bash
# Start Jupyter notebook
make jupyter
```

### Debugging Tests

```bash
# Run tests with verbose output
pytest -v

# Show print statements
pytest -s

# Drop into debugger on failure
pytest --pdb

# Run specific test with debugging
pytest tests/test_utils.py::test_get_device -v -s
```

## 📊 Coverage Reports

```bash
# Generate coverage report
make test-cov

# View HTML report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

## 🔄 Git Workflow

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new text classification model
fix: resolve memory leak in preprocessing
docs: update README with examples
test: add tests for utils module
refactor: simplify TextPreprocessor class
perf: optimize batch prediction
chore: update dependencies
```

### Pre-commit Hooks

Hooks run automatically before commits. To skip (not recommended):

```bash
git commit --no-verify
```

To run manually:

```bash
pre-commit run --all-files
```

## 🚢 Release Process

1. Update version in `src/nlp_research/__init__.py`
2. Update CHANGELOG
3. Create git tag
4. Build and publish

```bash
# Bump version
hatch version patch

# Build
make build

# Publish to Test PyPI
make publish-test

# Test installation
pip install -i https://test.pypi.org/simple/ nlp-research

# Publish to PyPI
make publish
```

## 📚 Additional Resources

- [Hatch Documentation](https://hatch.pypa.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pytest Documentation](https://docs.pytest.org/)
- [MyPy Documentation](https://mypy.readthedocs.io/)
- [Pre-commit Documentation](https://pre-commit.com/)

## 💡 Tips

1. Run `make pre-commit` before pushing to catch issues early
2. Use `make check-all` to run all quality checks
3. Write tests for new features
4. Update documentation when adding features
5. Keep dependencies up to date
6. Follow type hints and docstring conventions

## ❓ Getting Help

- Check `make help` for available commands
- Read error messages carefully
- Check GitHub Issues
- Review pre-commit output for specific fixes needed

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
