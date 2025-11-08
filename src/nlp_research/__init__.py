"""NLP Research Hub - Ultra-modern NLP research tools and utilities."""

__version__ = "0.1.0"
__author__ = "Umit Kacar"

from nlp_research.models import TextClassifier
from nlp_research.utils import count_parameters, get_device, load_config, save_config

__all__ = [
    "TextClassifier",
    "get_device",
    "load_config",
    "save_config",
    "count_parameters",
]

# Optional imports
try:
    from nlp_research.preprocessing import TextPreprocessor

    __all__.append("TextPreprocessor")
except ImportError:
    # spaCy not installed, TextPreprocessor not available
    pass
