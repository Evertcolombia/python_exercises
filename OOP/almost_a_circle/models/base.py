#!/usr/bin/python3

import json

class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if lis_dictionaries is not None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
