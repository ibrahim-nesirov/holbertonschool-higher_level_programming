#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.
    Args:
        text (str): The string to be formatted and printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_space = True
    for i, char in enumerate(text):
        if skip_space and char == ' ':
            continue
        skip_space = False
        if char in ".?:":
            print(char)
            remaining = text[i + 1:].lstrip(' ')
            if remaining:
                print()
            skip_space = True
        else:
            print(char, end="")
