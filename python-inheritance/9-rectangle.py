#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    """

    def __init__(self, width, height):
        """Initializes the Rectangle with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than or equal to 0.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).

        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle.

        Returns:
            str: A string in the format [Rectangle] width/height.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
