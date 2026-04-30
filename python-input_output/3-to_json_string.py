#!/usr/bin/python3
"""Module for to_json_string function."""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
