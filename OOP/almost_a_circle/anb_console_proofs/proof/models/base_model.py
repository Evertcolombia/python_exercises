#!/usr/bin/python3
"""
This is module define the base class (super class)
"""

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Class BaseModel

        Public attributes
            attr1 (id):  to count instances
    """

    def __init__(self, *args, **kwargs):
        """
        Validate values

        """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    formate = "%Y-%m-%dT%H:%M:%S.%f"
                    val = datetime.strptime(value, formate)
                    setattr(self, key, val)
                
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
            strng representation of the  instance
        """
        st = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return st

    def save(self):
        """
            update the instance update_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            return a dictionary representation of de obj inctance
        """
        new_d = self.__dict__.copy()
        new_d["__class__"] = __class__.__name
        new_d['created_at'] = self.created_at.isoformat()
        new_d['updated_at'] = self.updated_at.isoformat()

        return new_d

