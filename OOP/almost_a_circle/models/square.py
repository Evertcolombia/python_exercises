#!/usr/binpython3

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(__class__.__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validation_case("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for i, ar in enumerate(args):
                if i == 0:
                    self.id = ar
                if i == 1:
                    self.size = ar
                if i == 2:
                    self.x = ar
                if i == 3:
                    self.y = ar

        elif kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        l = ['id', 'size', 'x', 'y']
        d = {}

        for arg in l:
            a = {arg: getattr(self, arg)}
            d.update(a)

        return d
