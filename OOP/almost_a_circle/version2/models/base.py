#!/usr/bin/python3
"""
This module define the base class (super class)
"""


class Base:
    """Class Base

    Private attribute __nb_objects to count instances

    Attributes:
        battr1 (id): id of the instanc

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
