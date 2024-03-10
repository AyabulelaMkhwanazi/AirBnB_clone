#!/usr/bin/python3
"""
This module contains the class 'Amenity' that inherits from the 'BaseModel'.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class 'Amenity' inherits from the 'BaseModel'.

    Args:
        name (str): Amenity's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the 'Amenity' class.
        """
        super().__init__(*args, **kwargs)
