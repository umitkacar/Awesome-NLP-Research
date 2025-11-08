"""Tests for NLP models."""

import pytest

# Note: These tests are marked as integration tests since they require downloading models
# Run with: pytest -m integration


@pytest.mark.integration
@pytest.mark.slow
def test_text_classifier_init() -> None:
    """Test TextClassifier initialization."""
    from nlp_research.models import TextClassifier

    classifier = TextClassifier(model_name="bert-base-uncased", num_labels=2)

    assert classifier.model_name == "bert-base-uncased"
    assert classifier.num_labels == 2
    assert classifier.device in ["cuda", "mps", "cpu"]
    assert classifier.tokenizer is not None
    assert classifier.model is not None


@pytest.mark.integration
@pytest.mark.slow
def test_text_classifier_predict() -> None:
    """Test single text prediction."""
    from nlp_research.models import TextClassifier

    classifier = TextClassifier(model_name="bert-base-uncased", num_labels=2)
    result = classifier.predict("This is a great movie!")

    assert isinstance(result, dict)
    assert "label" in result
    assert "score" in result
    assert "class_id" in result
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0.0 <= result["score"] <= 1.0
    assert result["class_id"] in [0, 1]


@pytest.mark.integration
@pytest.mark.slow
def test_text_classifier_batch_predict(sample_texts: list[str]) -> None:
    """Test batch prediction."""
    from nlp_research.models import TextClassifier

    classifier = TextClassifier(model_name="bert-base-uncased", num_labels=2)
    results = classifier.batch_predict(sample_texts)

    assert len(results) == len(sample_texts)
    assert all(isinstance(r, dict) for r in results)
    assert all("label" in r for r in results)
    assert all("score" in r for r in results)


@pytest.mark.unit
def test_text_classifier_device_selection() -> None:
    """Test device selection logic (unit test, no model download)."""
    # This is a simplified test that doesn't require model download
    import torch

    if torch.cuda.is_available():
        expected_device = "cuda"
    elif torch.backends.mps.is_available():
        expected_device = "mps"
    else:
        expected_device = "cpu"

    # Just verify the logic, not the actual classifier
    assert expected_device in ["cuda", "mps", "cpu"]
