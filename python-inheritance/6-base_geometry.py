#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry-related classes.

    This class serves as a base for other geometry-related classes.
    It contains an unimplemented method area(), which is expected to
    be overridden by subclasses to compute the area of specific shapes.

    Methods:
        area(self): Raises an Exception indicating that this method
            must be implemented by subclasses.

    """

    def area(self):
        """Raises an exception: area() is not implemented.

        Raises:
            Exception: Always raises an exception with the message
                area() is not implemented.

        """
        raise Exception("area() is not implemented")
