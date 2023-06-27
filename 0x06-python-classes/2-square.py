#!/usr/bin/python3


class Square:
    """
    This class represents a square object. It has a single attribute, size,
    which determines the length of each side of the square.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size
