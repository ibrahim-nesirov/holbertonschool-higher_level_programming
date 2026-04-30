#!/usr/bin/python3
"""Module for SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin class that provides swimming ability."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying ability."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon class that can swim and fly."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
        