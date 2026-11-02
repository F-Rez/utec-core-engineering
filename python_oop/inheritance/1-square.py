#!/usr/bin/env python3
"""Define Square, a specialized Rectangle with equal sides."""
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
