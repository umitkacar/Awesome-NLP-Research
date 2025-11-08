"""Text preprocessing utilities for NLP tasks."""

import re
from typing import Any

try:
    import spacy
except ImportError as e:
    msg = (
        "spaCy is not installed. Install it with: "
        "pip install 'nlp-research[nlp]' or pip install spacy"
    )
    raise ImportError(msg) from e


class TextPreprocessor:
    """Text preprocessing pipeline for NLP tasks.

    Args:
        language: Language model to load (default: 'en_core_web_sm')
        lowercase: Whether to convert text to lowercase
        remove_punctuation: Whether to remove punctuation
        remove_stopwords: Whether to remove stopwords

    Example:
        >>> preprocessor = TextPreprocessor()
        >>> text = "This is a GREAT example!!! 🎉"
        >>> cleaned = preprocessor.clean(text)
        >>> print(cleaned)
        'great example'
    """

    def __init__(
        self,
        language: str = "en_core_web_sm",
        lowercase: bool = True,
        remove_punctuation: bool = True,
        remove_stopwords: bool = True,
    ) -> None:
        """Initialize the text preprocessor."""
        try:
            self.nlp = spacy.load(language)
        except OSError:
            # If model not found, provide helpful error message
            msg = (
                f"Language model '{language}' not found. "
                f"Please install it with: python -m spacy download {language}"
            )
            raise RuntimeError(msg) from None

        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_stopwords = remove_stopwords

    def clean(self, text: str) -> str:
        """Clean and preprocess text.

        Args:
            text: Input text to clean

        Returns:
            Cleaned text string
        """
        # Remove URLs
        text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)

        # Remove email addresses
        text = re.sub(r"\S+@\S+", "", text)

        # Remove mentions and hashtags
        text = re.sub(r"@\w+|#\w+", "", text)

        # Remove emojis and special characters
        text = re.sub(r"[^\w\s]", " " if not self.remove_punctuation else "", text)

        # Remove extra whitespace
        text = " ".join(text.split())

        # Process with spaCy
        doc = self.nlp(text)

        # Extract tokens with optional filtering
        tokens = []
        for token in doc:
            if self.remove_stopwords and token.is_stop:
                continue
            if self.remove_punctuation and token.is_punct:
                continue
            if token.is_space:
                continue

            token_text = token.text.lower() if self.lowercase else token.text
            tokens.append(token_text)

        return " ".join(tokens)

    def lemmatize(self, text: str) -> str:
        """Lemmatize text using spaCy.

        Args:
            text: Input text to lemmatize

        Returns:
            Lemmatized text string
        """
        doc = self.nlp(text)
        return " ".join([token.lemma_ for token in doc if not token.is_space])

    def extract_entities(self, text: str) -> list[dict[str, Any]]:
        """Extract named entities from text.

        Args:
            text: Input text to analyze

        Returns:
            List of dictionaries containing entity information
        """
        doc = self.nlp(text)
        return [
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
            }
            for ent in doc.ents
        ]
