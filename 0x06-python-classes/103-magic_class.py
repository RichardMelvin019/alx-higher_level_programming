#!/usr/bin/python3
"""Magic calculator. """
import math


class MagicClass:
    """Sets magic calculator"""

    def __init__(self, radius=0):
        """Magic calculator.  """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Magic calculator. """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Magic Calculator. """
        return 2 * math.pi * self.__radius
