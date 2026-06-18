#!/usr/bin/python3
"""Module for print_square function."""


def print_square(size):
    """Prints a square with the # character.

    Args:
        size: size length of the square.

    Raises:
        TypeError: If size is not an integer or is a float.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    if type(size) is float:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
