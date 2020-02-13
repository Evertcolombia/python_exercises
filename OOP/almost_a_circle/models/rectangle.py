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


    """ PUBLIC METHODS """

    def area(self):
        return self.__width * self.__height

    def display(self):
        print(('\n' * self.__y) + ((" " * self.__x) \
            + "#" * self.__width + '\n') * self.__height, end='')

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
                                        self.id,
                                        self.__x,
                                        self.__y,
                                        self.__width,
                                        self.__height)

    def update(self, *args, **kwargs):
        if args is not  None and len(args) > 0:
            for i, ar in enumerate(args):
                if i == 0:
                    super().__init__(ar)
                    self.id = ar
                if i == 1:
                    self.__width = ar
                if i == 2:
                    self.__height = ar
                if i == 3:
                    self.__x = ar
                if i == 4:
                    self.__y = ar
        
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        l = ['id', 'width', 'height', 'x', 'y']
        d = {}

        for arg in l:
            a = {arg: getattr(self, arg)}
            d.update(a)
        return d
