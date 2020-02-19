#!/usr/bin/python3
"""
This module define the class Review
"""


from datetime import datetime
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
    """Class State

       Public Attributes
           attr1 (place_id): id of the place reviewed - string
           attr2 (user_id): id of the user that review - string
           attr3 (text): the review - string
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
