#!/usr/bin/env python3
"""Define a complete Rectangle with area and string representation."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with a private width and height."""

    def __init__(self, width, height):
        """Validate and store the width and height of the rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description as [Rectangle] width/height."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
