#!/usr/bin/python3
"""A class that defines a rectangle. """


class Rectangle:
    """class of rectangle. """

    def __init__(self, width=0, height=0):
        """Initializing class of rectangle. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attribute. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle. """
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of the rectangle. """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
