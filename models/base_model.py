#!/usr/bin/python3
"""
Defines BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        initializes base model
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

        else:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for m, n in kwargs.items():
                if "__class__" not in m:
                    setattr(self, m, n)

    def __str__(self):
        
        """Returns string representation"""
        string = "["
        string += str(self.__class__.__name__) + '] ('
        string += str(self.id) + ') ' + str(self.__dict__)
        return string
   
    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary of baseModel instance"""
        bdict = self.__dict__.copy()
        bdict["created_at"] = self.created_at.isoformat()
        bdict["updated_at"] = self.updated_at.isoformat()
        bdict["__class__"] = self.__class__.__name__
        return bdict
