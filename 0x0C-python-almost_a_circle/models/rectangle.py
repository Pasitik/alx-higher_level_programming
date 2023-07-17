#!/usr/bin/python3

"""
Contains a Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """ A Base with a __init__ method """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing class or instance attributes

        Args:
            id (int): an integer assignable to self.id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value for width """
        if not isinstance(value, int):
            Rectangle.raiseNotIntegerError("width")
        if value <= 0:
            Rectangle.raiseValueLessThanOrEqualToZeroError("width")

        self.__width = value

    @property
    def height(self):
        """ get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value for height """
        if not isinstance(value, int):
            Rectangle.raiseNotIntegerError("height")
        if value <= 0:
            Rectangle.raiseValueLessThanOrEqualToZeroError("height")

        self.__height = value

    @property
    def x(self):
        """ get the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the value for x """
        if not isinstance(value, int):
            Rectangle.raiseNotIntegerError("x")
        if value < 0:
            Rectangle.raiseValueLessThanZeroError("x")

        self.__x = value

    @property
    def y(self):
        """ get the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the value for y """
        if not isinstance(value, int):
            Rectangle.raiseNotIntegerError("y")
        if value < 0:
            Rectangle.raiseValueLessThanZeroError("y")

        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        display the rectangle with # symbol
        based on the width and height
        """
        for i in range(self.__height):
            for x in range(self.__y):
                print()
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ return a string representation of this instance """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ update attributes of an instance in a certain order """

        for i in range(len(args)):
            if i == 0:
                self.__id = args[0]
            elif i == 1:
                self.__width = args[1]
            elif i == 2:
                self.__height = args[2]
            elif i == 3:
                self.__x = args[3]
            elif i == 4:
                self.__y = args[4]

        for key, value in kwargs.items():
            if key == "id":
                self.__id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value

    def to_dictionary(self):
        rect_dict = {}
        rect_dict["id"] = self.id
        rect_dict["width"] = self.width
        rect_dict["height"] = self.height
        rect_dict["x"] = self.x
        rect_dict["y"] = self.y

        return rect_dict
