#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize square with size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation.

        Args:
            value (int): The size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
