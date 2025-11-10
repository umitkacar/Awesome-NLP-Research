"""Utility functions for NLP research."""

import json
from pathlib import Path
from typing import Any, cast

import torch


def get_device() -> str:
    """Get the best available device for PyTorch.

    Returns:
        Device string ('cuda', 'mps', or 'cpu')

    Example:
        >>> device = get_device()
        >>> print(f"Using device: {device}")
        Using device: cuda
    """
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def load_config(config_path: str | Path) -> dict[str, Any]:
    """Load configuration from JSON file.

    Args:
        config_path: Path to the configuration file

    Returns:
        Configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If config file is not valid JSON

    Example:
        >>> config = load_config("config.json")
        >>> print(config['model_name'])
        bert-base-uncased
    """
    config_path = Path(config_path)

    if not config_path.exists():
        msg = f"Configuration file not found: {config_path}"
        raise FileNotFoundError(msg)

    with config_path.open(encoding="utf-8") as f:
        return cast("dict[str, Any]", json.load(f))


def save_config(config: dict[str, Any], config_path: str | Path) -> None:
    """Save configuration to JSON file.

    Args:
        config: Configuration dictionary to save
        config_path: Path where to save the configuration

    Example:
        >>> config = {"model_name": "bert-base-uncased", "num_labels": 2}
        >>> save_config(config, "config.json")
    """
    config_path = Path(config_path)
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)


def count_parameters(model: torch.nn.Module) -> int:
    """Count the number of trainable parameters in a model.

    Args:
        model: PyTorch model

    Returns:
        Number of trainable parameters

    Example:
        >>> from transformers import AutoModel
        >>> model = AutoModel.from_pretrained("bert-base-uncased")
        >>> params = count_parameters(model)
        >>> print(f"Model has {params:,} trainable parameters")
        Model has 109,482,240 trainable parameters
    """
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
