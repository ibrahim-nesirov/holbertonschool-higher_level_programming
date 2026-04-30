#!/usr/bin/python3
"""Module for abstract Animal class and subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return Bark."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return Meow."""
        return "Meow"
    