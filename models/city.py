#!/usr/bin/python3
"""
This module define the class City
"""


from datetime import datetime
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""
    """Class City

       Public Attributes
           attr1 (state_id): id of the State - string
           attr2 (name): name of the City - string
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
