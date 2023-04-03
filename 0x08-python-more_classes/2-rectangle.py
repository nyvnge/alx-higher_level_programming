#!/usr/bin/python3
"""This defines a rectangle class"""


class Rectangle:
    """This represent a rectangle."""

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """This initializes a new Rectangle.
        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.width = width
        self.height = height
        self.__area = 0
        self.__perimeter = 0

    @property
    def width(self) -> int:
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer {value}")
        if value < 0:
            raise ValueError(f"width must be >= 0 {value}")
        self.__width = value
        self.__area = 0
        self.__perimeter = 0

    @property
    def height(self) -> int:
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer {value}")
        if value < 0:
            raise ValueError(f"height must be >= 0 {value}")
        self.__height = value
        self.__area = 0
        self.__perimeter = 0

    def area(self) -> int:
        """Return the area of the Rectangle."""
        if self.__area == 0:
            self.__area = self.__width * self.__height
        return self.__area

    def perimeter(self) -> int:
        """Return the perimeter of the Rectangle."""
        if self.__perimeter == 0:
            if self.__width == 0 or self.__height == 0:
                self.__perimeter = 0
            else:
                self.__perimeter = 2 * (self.__width + self.__height)
        return self.__perimeter
