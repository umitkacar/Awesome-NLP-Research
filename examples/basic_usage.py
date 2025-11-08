"""Basic usage examples for NLP Research Hub."""

from nlp_research import TextClassifier, TextPreprocessor, get_device


def main() -> None:
    """Run basic examples."""
    # Show available device
    print(f"Using device: {get_device()}\n")

    # Example 1: Text Classification
    print("=" * 60)
    print("Example 1: Text Classification")
    print("=" * 60)

    # Note: First run will download the model
    classifier = TextClassifier("bert-base-uncased", num_labels=2)

    texts = [
        "This movie is absolutely amazing! I loved it!",
        "Terrible product. Would not recommend.",
        "It's okay, nothing special.",
    ]

    for text in texts:
        result = classifier.predict(text)
        print(f"\nText: {text}")
        print(f"Prediction: {result['label']} (confidence: {result['score']:.4f})")

    # Example 2: Text Preprocessing
    print("\n" + "=" * 60)
    print("Example 2: Text Preprocessing")
    print("=" * 60)

    # Note: Requires spacy model installation
    # Run: python -m spacy download en_core_web_sm
    try:
        preprocessor = TextPreprocessor()

        raw_text = """
        Check out https://example.com! 🎉
        Contact us at info@example.com
        This is AMAZING!!! @user #hashtag
        """

        print(f"\nOriginal text:\n{raw_text}")

        cleaned = preprocessor.clean(raw_text)
        print(f"\nCleaned text:\n{cleaned}")

        # Extract entities
        entity_text = "Apple Inc. was founded by Steve Jobs in California"
        entities = preprocessor.extract_entities(entity_text)

        print(f"\nEntity extraction from: {entity_text}")
        for entity in entities:
            print(f"  - {entity['text']:20s} ({entity['label']})")

    except RuntimeError as e:
        print(f"\nPreprocessing example skipped: {e}")
        print("Install spacy model with: python -m spacy download en_core_web_sm")


if __name__ == "__main__":
    main()
