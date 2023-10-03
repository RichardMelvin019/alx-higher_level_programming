#!/usr/bin/python3
"""A class that defines a rectangle. """


class Rectangle:
    """class of rectangle. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing class of rectangle. """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self) -> str:
        """Presents a diagram of rectangle. """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_1 = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle_1 += str(self.print_symbol)
                except Exception:
                    rectangle_1 += type(self).print_symbol
            if column < self.__height - 1:
                rectangle_1 += "\n"
        return (rectangle_1)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message for objects deleted. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
