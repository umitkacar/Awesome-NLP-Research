"""Tests for utility functions."""

import json
from pathlib import Path

import pytest
import torch

from nlp_research.utils import count_parameters, get_device, load_config, save_config


def test_get_device() -> None:
    """Test get_device function returns valid device."""
    device = get_device()
    assert device in ["cuda", "mps", "cpu"]


def test_save_and_load_config(tmp_path: Path, config_dict: dict[str, str | int]) -> None:
    """Test saving and loading configuration."""
    config_path = tmp_path / "config.json"

    # Save config
    save_config(config_dict, config_path)
    assert config_path.exists()

    # Load config
    loaded_config = load_config(config_path)
    assert loaded_config == config_dict


def test_load_config_file_not_found() -> None:
    """Test load_config raises FileNotFoundError for missing file."""
    with pytest.raises(FileNotFoundError, match="Configuration file not found"):
        load_config("nonexistent.json")


def test_load_config_invalid_json(tmp_path: Path) -> None:
    """Test load_config raises JSONDecodeError for invalid JSON."""
    invalid_json = tmp_path / "invalid.json"
    invalid_json.write_text("not valid json")

    with pytest.raises(json.JSONDecodeError):
        load_config(invalid_json)


def test_count_parameters() -> None:
    """Test counting model parameters."""
    # Create a simple model
    model = torch.nn.Sequential(
        torch.nn.Linear(10, 20),
        torch.nn.ReLU(),
        torch.nn.Linear(20, 5),
    )

    param_count = count_parameters(model)
    # Linear(10, 20) = 10*20 + 20 = 220
    # Linear(20, 5) = 20*5 + 5 = 105
    # Total = 325
    assert param_count == 325


def test_count_parameters_frozen_weights() -> None:
    """Test counting parameters excludes frozen weights."""
    model = torch.nn.Linear(10, 5)

    # Freeze all parameters
    for param in model.parameters():
        param.requires_grad = False

    param_count = count_parameters(model)
    assert param_count == 0
