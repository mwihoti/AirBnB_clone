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
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'W', encoding='utf-8') as stor:
            json.dump(dictionary, stor)
    def reload(self):
        """
          deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as rld:
                my_obj = rld.read()
        except Exception:
            return
        objects = eval(my_obj)
        for (key, value) in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
            self.__objects = objects