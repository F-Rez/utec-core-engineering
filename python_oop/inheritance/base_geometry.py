#!/usr/bin/env python3
"""Define BaseGeometry, the parent class for geometric shapes."""


class BaseGeometry:
    """Provide behavior shared by all geometric shapes."""

    def area(self):
        """Raise an exception because each shape computes its own area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
