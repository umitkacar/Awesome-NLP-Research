"""Tests for text preprocessing."""

import pytest

from nlp_research.preprocessing import TextPreprocessor


@pytest.fixture
def preprocessor() -> TextPreprocessor:
    """Create a TextPreprocessor instance for testing.

    Returns:
        TextPreprocessor instance
    """
    # Note: This will fail if spacy model not installed
    # Skip test if model not available
    try:
        return TextPreprocessor()
    except RuntimeError:
        pytest.skip("spaCy model not installed")


def test_preprocessor_clean_basic(preprocessor: TextPreprocessor) -> None:
    """Test basic text cleaning."""
    text = "This is a GREAT example!!!"
    cleaned = preprocessor.clean(text)

    assert isinstance(cleaned, str)
    assert len(cleaned) > 0
    assert "GREAT" not in cleaned  # Should be lowercased
    assert "!!!" not in cleaned  # Punctuation should be removed


def test_preprocessor_clean_urls(preprocessor: TextPreprocessor) -> None:
    """Test URL removal."""
    text = "Check out https://example.com for more info"
    cleaned = preprocessor.clean(text)

    assert "https://example.com" not in cleaned
    assert "example.com" not in cleaned


def test_preprocessor_clean_emails(preprocessor: TextPreprocessor) -> None:
    """Test email removal."""
    text = "Contact me at test@example.com"
    cleaned = preprocessor.clean(text)

    assert "test@example.com" not in cleaned


def test_preprocessor_lemmatize(preprocessor: TextPreprocessor) -> None:
    """Test text lemmatization."""
    text = "The cats are running quickly"
    lemmatized = preprocessor.lemmatize(text)

    assert isinstance(lemmatized, str)
    # spaCy should lemmatize 'cats' -> 'cat', 'running' -> 'run'


def test_preprocessor_extract_entities(preprocessor: TextPreprocessor) -> None:
    """Test named entity extraction."""
    text = "Apple Inc. was founded by Steve Jobs in California"
    entities = preprocessor.extract_entities(text)

    assert isinstance(entities, list)
    assert all(isinstance(ent, dict) for ent in entities)

    # Check entity structure
    if entities:
        assert "text" in entities[0]
        assert "label" in entities[0]
        assert "start" in entities[0]
        assert "end" in entities[0]


def test_preprocessor_init_invalid_model() -> None:
    """Test initialization with invalid language model."""
    with pytest.raises(RuntimeError, match="Language model.*not found"):
        TextPreprocessor(language="invalid_model_name")
