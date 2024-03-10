#!/usr/bin/python3
"""
This module contains a class 'City' that inherits from the 'BaseModel'.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class 'City' inherits from the 'BaseModel'.

    Args:
        state_id (str): The State's id.
        name (str): The city's name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the 'City' class.
        """
        super().__init__(*args, **kwargs)
