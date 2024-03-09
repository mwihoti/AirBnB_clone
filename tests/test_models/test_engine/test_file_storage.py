#!/usr/bin/python3
import unittest
import os
import models

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()
        self.user = User()
        self.amenity = Amenity()
        self.state = State()
        self.city = City()
        self.place = Place()
        self.review = Review()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        del self.base
        del self.user
        del self.amenity
        del self.state
        del self.city
        del self.place
        del self.review
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        check = self.storage.all()
        self.assertIsNotNone(check)
        self.assertEqual(type(check), dict)

    def test_new(self):
        check = self.storage.all()
        self.user.name = "Mwihoti"
        self.user.id = "1234"
        check2 = self.storage.new(self.user)
        val = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.assertIsNotNone(check[val])


if __name__ == "__main__":
    unittest.main()
