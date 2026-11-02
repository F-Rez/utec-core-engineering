#!/usr/bin/env python3
"""Module that defines a Square class with a position and string output."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: The size of the square's side (default 0).
            position: Tuple (x, y) offset used when printing (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it.

        Args:
            value: The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating it.

        Args:
            value: A tuple of 2 non-negative integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square to stdout using '#', offset by position.

        Prints an empty line if size is 0.
        """
        print(self)

    def __str__(self):
        """Return the square as a string, same as my_print output."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines += [row] * self.__size
        return "\n".join(lines)
