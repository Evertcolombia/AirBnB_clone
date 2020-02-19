#!/usr/bin/python3
"""
This module define the class user
"""


from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
