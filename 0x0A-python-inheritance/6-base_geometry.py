#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """Raises a TypeError if called"""
        raise TypeError("area() is not implemented")

