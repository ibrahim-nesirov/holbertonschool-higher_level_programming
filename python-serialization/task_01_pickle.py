#!/usr/bin/python3
"""Module for CustomObject class with pickle serialization."""
import pickle


class CustomObject:
    """A custom class that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file.

        Args:
            filename (str): The filename to save the object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Args:
            filename (str): The filename to load the object from.

        Returns:
            CustomObject: The deserialized object or None.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
