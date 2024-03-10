#!/usr/bin/python3
"""
This module contains a class 'State' that inherits from 'BaseModel'.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class 'State' inherits from 'BaseModel'.

    Args:
        name (str): State's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the 'State' class.
        """
        super().__init__(*args, **kwargs)
