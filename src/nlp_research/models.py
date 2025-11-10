"""NLP models for text classification and analysis."""

from typing import Any

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


class TextClassifier:
    """Text classification using transformer models.

    Args:
        model_name: Name of the pretrained model from Hugging Face Hub
        num_labels: Number of classification labels
        device: Device to run the model on ('cpu' or 'cuda')

    Example:
        >>> classifier = TextClassifier("bert-base-uncased", num_labels=2)
        >>> result = classifier.predict("This is a great movie!")
        >>> print(result)
        {'label': 'POSITIVE', 'score': 0.9998}
    """

    def __init__(
        self,
        model_name: str = "bert-base-uncased",
        num_labels: int = 2,
        device: str | None = None,
    ) -> None:
        """Initialize the text classifier."""
        self.model_name = model_name
        self.num_labels = num_labels
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        # Note: For production use, pin model revisions using revision="commit_hash"
        # Example: AutoTokenizer.from_pretrained(model_name, revision="abc123")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)  # nosec B615
        self.model = AutoModelForSequenceClassification.from_pretrained(  # nosec B615
            model_name,
            num_labels=num_labels,
        )
        self.model.to(self.device)
        self.model.eval()

    def predict(self, text: str) -> dict[str, Any]:
        """Predict the class of the input text.

        Args:
            text: Input text to classify

        Returns:
            Dictionary containing the predicted label and confidence score
        """
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        )
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=-1)
            predicted_class = torch.argmax(probabilities, dim=-1).item()
            confidence = probabilities[0][predicted_class].item()

        label = "POSITIVE" if predicted_class == 1 else "NEGATIVE"

        return {
            "label": label,
            "score": confidence,
            "class_id": predicted_class,
        }

    def batch_predict(self, texts: list[str]) -> list[dict[str, Any]]:
        """Predict classes for a batch of texts.

        Args:
            texts: List of input texts to classify

        Returns:
            List of dictionaries containing predictions for each text
        """
        return [self.predict(text) for text in texts]
