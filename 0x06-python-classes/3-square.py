#!/usr/bin/python3
"""Defines a Square. """


class Square:
    """A class representing a square. """

    def __init__(self, size=0):
        """Initializing the size of the Square. """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculates area of the class Square. """

        return (self.__size ** 2)
