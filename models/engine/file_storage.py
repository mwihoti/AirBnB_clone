#!/usr/bin/python3
"""Defines FileStorage module."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines FileStorage class """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the __objects"""
        return (self.__objects)

    def new(self, ob):
        """
          sets  __objects the ob with key
        """
        self.__objects["{}.{}".format(type(ob).__name__, ob.id)] = ob

    def save(self):
        """
           serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w') as s:
            dict_objects = {}
            for k, v in self.__objects.items():
                dict_objects[k] = v.to_dict()
            json.dump(dict_objects, s)

    def reload(self):
        """
          deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as rld:
                for objects in json.load(rld).values():
                    self.new(eval(objects["__class__"])(**objects))
        except FileNotFoundError:
            return
