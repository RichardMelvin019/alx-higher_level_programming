#!/usr/bin/python3
"""Defines a Square. """


class Square:
    """Defines a class Square. """

    def __init__(self, size=0):
        """Initializing the size of the square. """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of sqaure. """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square. """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of a square. """

        return (self.__size ** 2)
