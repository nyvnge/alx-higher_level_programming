#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Contains public instance methods area and integer validator"""

    def area(self):
        """Exception raised when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a parameter is an integer and is > 0. When defaulted it            will raise the following errors:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
