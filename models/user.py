#!/usr/bin/python3
"""
This module define the class user
"""


from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """Class User

       Public Attributes
           attr1 (email): email of the user - string
           attr2 (password): password of the user - string
           attr3 (first_name): firts name of the user - string
           attr4 (last_name): last name of the user - string
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
