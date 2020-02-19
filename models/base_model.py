#!/usr/bin/python3
"""
This is module define the base class (super class)
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """Class BaseModel

        Public attributes
            attr1 (id):  to count instances
            attr2 (created_at): control de date time for instances
            attr3 (updated_at): control de ptade datetime
    """

    def __init__(self, *args, **kwargs):
        """
        Validate values

        """
        if (kwargs):
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
                elif (key != '__class__'):
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            strng representation of the  instance
        """
        st = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                   self.__dict__)
        return st

    def save(self):
        """
            update the instance update_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            return a dictionary representation of de obj inctance
        """
        new_d = self.__dict__.copy()
        new_d["__class__"] = self.__class__.__name__
        new_d['created_at'] = self.created_at.isoformat('T')
        new_d['updated_at'] = self.updated_at.isoformat('T')

        return new_d
