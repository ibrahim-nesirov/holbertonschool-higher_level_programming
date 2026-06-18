#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size):
        """Initializes a new Square object.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).

        """
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: The string in the format [Square] size/size.

        """
        return "[Square] {}/{}".format(self.__size, self.__size)
