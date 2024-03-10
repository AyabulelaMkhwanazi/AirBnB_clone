#!/usr/bin/python3
"""
This module contains a class 'User' that inherits from the BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    'User' class that inherits from the BaseModel class.

    Args:
        email (str): User's email address.
        password (str): User's password
        first_name (str): User's first name
        last_name (str): User's last name (surname)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes the User class.
        """
        super().__init__(*args, **kwargs)
