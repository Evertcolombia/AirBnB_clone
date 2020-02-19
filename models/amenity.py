#!/usr/bin/python3
"""
This module define the class Amenity
"""


from datetime import datetime
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
    """Class Amenity

       Public Attributes
           attr1 (name): name of the amenity - string
    """

    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                elif (key != '__class__'):
                    setattr(self, key, value)
        else:
            super().__init__()
