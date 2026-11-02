#!/usr/bin/env python3
"""Define Square with its own string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a private size."""

    def __init__(self, size):
        """Validate size and initialize the parent Rectangle with it."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description as [Square] width/height."""
        return "[Square] {}/{}".format(self.__size, self.__size)
