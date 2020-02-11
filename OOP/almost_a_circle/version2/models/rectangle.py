#!/usr/bin/python3
"""
    This is module define the Square class
"""

from models.base import Base

class Rectangle(Base):
    """Class Rectangle

    Attributes:
        attr1 (width): width size for rectangle
        attr2 (height): height size for rectangle
        attr3 (x): x cordenade
        attr1 (y): y cordenade
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width (self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value


    def validator(self, name, value):
        if type(value) != int:
            raise TypeError ("{} must be an integer".format(name))
        if (name == "width") or (name == "height"):
            if  value < 0:
                raise ValueError ("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError ("{} must be >= 0".format(name))
            

    def area(self):
        return self.__width * self.__height

    def display(self):
        w = self.__width
        h = self.__height
        st = (("#" * w + '\n') * self.__height)
        print(st, end="")
