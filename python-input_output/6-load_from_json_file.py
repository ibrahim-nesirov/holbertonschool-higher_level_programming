#!/usr/bin/python3
"""Module for load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: Python data structure from the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
