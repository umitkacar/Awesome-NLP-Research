#!/bin/bash
# Setup script for NLP Research Hub

set -e

echo "🚀 Setting up NLP Research Hub..."

# Check Python version
echo "Checking Python version..."
python --version

# Install Hatch
echo "Installing Hatch..."
pip install hatch

# Install development dependencies
echo "Installing development dependencies..."
pip install -e ".[dev]"

# Install pre-commit hooks
echo "Setting up pre-commit hooks..."
pre-commit install

# Download spaCy model (optional)
read -p "Do you want to download spaCy English model? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Downloading spaCy model..."
    python -m spacy download en_core_web_sm
fi

# Run pre-commit on all files
echo "Running pre-commit checks..."
pre-commit run --all-files || true

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  - Run tests: make test"
echo "  - Format code: make format"
echo "  - Run linting: make lint"
echo "  - See all commands: make help"
