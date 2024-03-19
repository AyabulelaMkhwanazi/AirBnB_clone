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
        key = obj.__class__.__name__
        self.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj = self.__objects
        serialized_objects = {objs: obj[objs].to_dict()
                              for objs in obj.keys()}
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
                for value in data.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
