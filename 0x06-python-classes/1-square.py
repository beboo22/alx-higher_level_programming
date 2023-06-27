#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    This class represents a square object. It has a single attribute, size,
    which determines the length of each side of the square.
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self._size = size
