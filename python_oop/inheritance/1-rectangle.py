#!/usr/bin/env python3
"""Define Rectangle, a shape built on top of BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with a private width and height."""

    def __init__(self, width, height):
        """Validate and store the width and height of the rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
