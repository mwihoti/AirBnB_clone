#!/usr/bin/python3
"""
Defines city test
"""

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """
    class TestCity
    """

    def test_city_model_inheritance(self):
        """
        Test that city class inherits from BaseModel
        """

        new = City()
        self.assertIsInstance(new, BaseModel)

    def test_city_attr(self):
        """
        Test if city has name & id attributes
        """
        new = City()
        self.assertTrue("state_id" in new.__dir__())
        self.assertTrue("name" in new.__dir__())

    def test_city_str(self):
        """
        Check if city  attr is a string
        """
        new = City()
        nm_str = getattr(new, "name")
        self.assertIsInstance(nm_str, str)


if __name__ == '__main__':
    unittest.main()
