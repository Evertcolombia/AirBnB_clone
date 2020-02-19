#!/usr/bin/python3
"""
This module define the class state
"""


from datetime import datetime
from models.base_model import BaseModel


class State(BaseModel):
    name = ""
    """Class State

       Public Attributes
           attr1 (name): name of the state - string
    """

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
