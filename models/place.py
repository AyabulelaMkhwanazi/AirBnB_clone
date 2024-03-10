#!/usr/bin/python3
"""
This module contains a class 'Place' that inherits from the 'BaseModel'.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class 'Place' inherits from the 'BaseModel'.

    Args:
        city_id (str): The city's id.
        user_id (str): The user's id.
        name (str): The place's name
        description (str): Description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum amount of guests in the place.
        price_by_night (int): The price charged for the place per night.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
        amenity_ids ([str]): The list of amenity.id
    """
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

    def __init__(self, *args, **kwargs):
        """
        Initializes the class 'Place'.
        """
        super().__init__(*args, **kwargs)
