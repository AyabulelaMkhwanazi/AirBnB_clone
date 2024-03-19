#!/usr/bin/python3
"""
This module contains a class 'BaseModel' that defines all common attributes/
methods for other classes.
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    to inherit from.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class with a unique id and the current
        datetime for 'created_at' and 'updated_at'.

        id (str): assigns a unique id for each BaseModel
        created_at: assigns the current datetime when an instance is
                created.
        updated_at: assigns the current datetime when an instance is
            created and it wil be updated every time the object is changed.

        If kwargs is not empty, sets each key-value pair as an attribute-
        value pair, except for '__class__'
        """
        time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, time)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of BaseModel instance in the format:
        [<class name>] (<self.id>) <self.__dict__>
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at'
        with the current datetime. This method should be called whenever the
        object is saved.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of the instance's
        dictionary. The dictionary includes:
        - All instance attributes.
        - The class name under the key '__class__'.
        - The 'created_at' and 'updated_at' attributes converted to string in
        ISO format.

        This method is used for serialization/deserialization processes.
        """
        # start with the instance's dictionary
        dictionary = self.__dict__.copy()
        # convert 'created_at' to ISO format
        dictionary['created_at'] = self.created_at.isoformat()
        # convert 'updated_at' to ISO format
        dictionary['updated_at'] = self.updated_at.isoformat()
        # add the class name
        dictionary['__class__'] = self.__class__.__name__
        # return the dictionary
        return dictionary
