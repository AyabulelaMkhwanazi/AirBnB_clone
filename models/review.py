#!/usr/bin/python3
"""
This module contains a class 'Review' that inherits from the 'BaseModel'.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class 'Review' inherits from the 'BaseModel' class.

    Args:
        place_id (str): the name of the place to review.
        user_id (str): the user's id.
        text (str): the review text.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the 'Review' class.
        """
        super().__init__(*args, **kwargs)
