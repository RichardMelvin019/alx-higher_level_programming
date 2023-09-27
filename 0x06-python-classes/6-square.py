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

    @property
    def position(self):
        """Property of the cordinates of this square. """

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this square. """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of a square. """
        return self.__size * self.__size

    def pos_print(self):
        """Returns the position with spaces. """
        position_1 = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            position_1 += "\n"
        for x in range(self.size):
            for m in range(self.postion[0]):
                position_1 += " "
            for n in range(self.size):
                position_1 += "#"
            position_1 += "\n"
        return position_1

    def my_print(self):
        """Prints the square in the position. """

        print(self.pos_print(), end='')
