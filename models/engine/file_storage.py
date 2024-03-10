#!/usr/bin/python3
"""
This module contains a class 'FileStorage' that serializes instances to a JSON
file and deserializes JSON file to instances.
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to
    instances.
    """

    def __init__(self):
        """
        Initializes the FileStorage class.

        __file_path (str): path to the JSON file.
        __objects: stores all objects by <class name>.id
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized_objects = {}
        # iterate over eaach item in self.__objects
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, mode="w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists).
        """
        try:
            with open(self.__file_path, mode="r") as file:
                # load the data from the file
                data = json.load(file)
                deserialized_objects = {}
                # iterate over each item in the data
                for key, value in data.items():
                    # get the class name from the key
                    class_name = key.split('.')[0]
                    # convert the dict to an object of the appr. class & store
                    if class_name == "BaseModel":
                        deserialized_objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        deserialized_objects[key] = User(**value)
                    elif class_name == "Place":
                        deserialized_objects[key] = Place(**value)
                    elif class_name == "State":
                        deserialized_objects[key] = State(**value)
                    elif class_name == "City":
                        deserialized_objects[key] = City(**value)
                    elif class_name == "Amenity":
                        deserialized_objects[key] = Amenity(**value)
                    elif class_name == "Review":
                        deserialized_objects[key] = Review(**value)
                # assign the deserialized objects dictionary to self.__objects
                self.__objects = deserialized_objects
        except FileNotFoundError:
            pass
