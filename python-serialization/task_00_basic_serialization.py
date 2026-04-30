#!/usr/bin/python3
"""Module for basic serialization functions."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to a JSON file.

    Args:
        data (dict): A Python dictionary with data.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized data.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
