#!/usr/bin/python3
"""Module for from_json_string function."""
import json


def from_json_string(my_str):
    """Return Python object represented by a JSON string.

    Args:
        my_str (str): JSON string to deserialize.

    Returns:
        object: Python data structure.
    """
    return json.loads(my_str)
