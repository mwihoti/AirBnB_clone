#!/usr/bin/python3
"""
Defines place test
"""

import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    class TestPlace
    """
    def setUp(self):
        """
        creates place instance
        """
        self.new = Place()

    def tearDown(self):
        """
        clears after test
        """
        del self.new

    def test_place_model_inheritance(self):
        """
        Test if review class inherits from BaseModel
        """

        self.assertIsInstance(self.new, BaseModel)

    def test_place_attr(self):
        """
        Test if state has name attribute
        """

        place_attributes = [
            "city_id", "user_id", "description", "name",
            "number_rooms", "max_guest", "price_by_night",
            "latitude", "longitude", "amenity_ids"
        ]
        for attr in place_attributes:
            self.assertTrue(hasattr(self.new, attr))

    def test_attribute_types(self):
        """
        Test types of attributes in Place class.
        """
        self.assertIsInstance(self.new.amenity_ids, list)
        self.assertIsInstance(self.new.longitude, float)
        self.assertIsInstance(self.new.latitude, float)
        self.assertIsInstance(self.new.price_by_night, int)
        self.assertIsInstance(self.new.max_guest, int)
        self.assertIsInstance(self.new.number_bathrooms, int)
        self.assertIsInstance(self.new.number_rooms, int)
        self.assertIsInstance(self.new.description, str)
        self.assertIsInstance(self.new.name, str)
        self.assertIsInstance(self.new.user_id, str)
        self.assertIsInstance(self.new.city_id, str)


if __name__ == "__main__":
    unittest.main()
