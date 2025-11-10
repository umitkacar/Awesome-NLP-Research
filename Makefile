.PHONY: help install dev-install clean test test-cov lint format type-check pre-commit build docs serve-docs

.DEFAULT_GOAL := help

PYTHON := python3
HATCH := hatch

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ============================================================================
# Installation
# ============================================================================

install: ## Install package
	pip install -e .

dev-install: ## Install package with development dependencies
	pip install -e ".[dev]"
	pre-commit install

all-install: ## Install package with all dependencies
	pip install -e ".[all]"
	pre-commit install

# ============================================================================
# Cleaning
# ============================================================================

clean: ## Clean build artifacts and cache files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# ============================================================================
# Testing
# ============================================================================

test: ## Run tests
	$(HATCH) run test

test-parallel: ## Run tests in parallel
	$(HATCH) run test-parallel

test-cov: ## Run tests with coverage
	$(HATCH) run test-cov

test-cov-parallel: ## Run tests with coverage in parallel
	$(HATCH) run test-cov-parallel

test-unit: ## Run only unit tests
	$(HATCH) run test -m unit

test-integration: ## Run only integration tests
	$(HATCH) run test -m integration

test-fast: ## Run fast tests (not slow, not integration)
	$(HATCH) run test -m "not slow and not integration"

test-watch: ## Run tests in watch mode
	$(HATCH) run pytest-watch

# ============================================================================
# Code Quality
# ============================================================================

lint: ## Lint code with ruff
	$(HATCH) run lint:check

format: ## Format code with ruff and black
	$(HATCH) run lint:format

type-check: ## Type check with mypy
	mypy src/

check-all: lint type-check test ## Run all checks (lint, type-check, test)

# ============================================================================
# Pre-commit
# ============================================================================

pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	pre-commit autoupdate

# ============================================================================
# Build & Release
# ============================================================================

build: clean ## Build package distribution
	$(HATCH) build

publish-test: build ## Publish to Test PyPI
	$(HATCH) publish -r test

publish: build ## Publish to PyPI
	$(HATCH) publish

# ============================================================================
# Documentation
# ============================================================================

docs: ## Build documentation
	$(HATCH) run docs:build

serve-docs: ## Serve documentation locally
	$(HATCH) run docs:serve

# ============================================================================
# Development
# ============================================================================

shell: ## Start IPython shell with package loaded
	ipython -i -c "from nlp_research import *"

jupyter: ## Start Jupyter notebook
	jupyter notebook

setup-dev: dev-install pre-commit ## Complete development setup
	@echo "Development environment setup complete!"

# ============================================================================
# Docker (if needed)
# ============================================================================

docker-build: ## Build Docker image
	docker build -t nlp-research:latest .

docker-run: ## Run Docker container
	docker run -it --rm nlp-research:latest

# ============================================================================
# Version Management
# ============================================================================

version: ## Show current version
	@$(HATCH) version

bump-patch: ## Bump patch version (0.1.0 -> 0.1.1)
	@$(HATCH) version patch

bump-minor: ## Bump minor version (0.1.0 -> 0.2.0)
	@$(HATCH) version minor

bump-major: ## Bump major version (0.1.0 -> 1.0.0)
	@$(HATCH) version major
