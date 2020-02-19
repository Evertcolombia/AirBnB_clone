#!/usr/bin/python3
"""
This module define the class Place
"""


from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    """Class Place

       Public Attributes
           attr1 (city_id): id of the city - string
           attr2 (user_id): id of the own user  - string
           attr3 (name): name of the place - string
           attr4 (description): description of the place - integer
           attr5 (number_rooms): number of rooms - integer
           attr6 (number_bathrooms): number of wc - integer
           attr7 (max_guest): max number of people - integer
           attr8 (price_by_night): price by night - integer
           attr9 (latitude): latitud - float
           attr10 (longitude): longitude - float
           attr11 (amenity_ids): ids of the amenities - list of strings
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
