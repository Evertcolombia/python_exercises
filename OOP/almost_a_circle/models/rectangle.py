#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
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
    def width(self, value):
        self.validation_case("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        self.validation_case("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @width.setter
    def x(self, value):
        self.validation_case("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @width.setter
    def y(self, value):
        self.validation_case("y", value)
        self.__y = value

    def validation_case(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer". format(name))

        if name == "width" or name == "heigth":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.__width * self.__height
