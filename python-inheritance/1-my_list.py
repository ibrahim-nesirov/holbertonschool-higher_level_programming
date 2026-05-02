#!/usr/bin/python3
"""Module that defines MyList class that inherits from list"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
