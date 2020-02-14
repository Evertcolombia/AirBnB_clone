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
            attr2 (create_at): control de date time for instances
            attr3 (update_at): control de ptade datetime
    """

    def __init__(self):
        """
        Validate values

        """
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()

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
        self.update_at = datetime.now()

    def to_dict(self):
        """
            return a dictionary representation of de obj inctance
        """
        new_d = self.__dict__.copy()
        new_d["__class__"] = __class__.__name__
        new_d['create_at'] = self.create_at.isoformat()
        new_d['update_at'] = self.update_at.isoformat()

        return new_d
