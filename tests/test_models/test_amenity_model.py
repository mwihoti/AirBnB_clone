#!/usr/bin/python3
"""
Defines Amenity test
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    class TestAmenity
    """

    def test_amenity_model_inheritance(self):
        """
        Test that amenity class inherits from BaseModel
        """

        new = Amenity()
        self.assertIsInstance(new, BaseModel)

    def test_amenity_attr(self):
        """
        Test if amenity has name attribute
        """
        new = Amenity()
        self.assertTrue("name" in new.__dir__())

    def test_amenity_str(self):
        """
        Check if attr is a string
        """
        new = Amenity()
        nm_str = getattr(new, "name")
        self.assertIsInstance(nm_str, str)


if __name__ == '__main__':
    unittest.main()
