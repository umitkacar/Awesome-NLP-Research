"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_text() -> str:
    """Return a sample text for testing.

    Returns:
        Sample text string
    """
    return "This is a great example of natural language processing!"


@pytest.fixture
def sample_texts() -> list[str]:
    """Return multiple sample texts for testing.

    Returns:
        List of sample text strings
    """
    return [
        "I love this product! It's amazing.",
        "This is terrible. I hate it.",
        "The movie was okay, nothing special.",
    ]


@pytest.fixture
def config_dict() -> dict[str, str | int]:
    """Return a sample configuration dictionary.

    Returns:
        Configuration dictionary
    """
    return {
        "model_name": "bert-base-uncased",
        "num_labels": 2,
        "max_length": 512,
    }
