#!/usr/bin/python3
"""
Defines state test
"""

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """
    class TestReview
    """

    def test_Review_model_inheritance(self):
        """
        Test that state class inherits from BaseModel
        """

        new = Review()
        self.assertIsInstance(new, BaseModel)

    def test_review_attr(self):
        """
        Test if state has name attribute
        """
        new = Review()
        self.assertTrue("place_id" in new.__dir__())
        self.assertTrue("user_id" in new.__dir__())
        self.assertTrue("text" in new.__dir__())



    def test_state_str(self):
        """
        Check if attr is a string
        """
        new = Review()
        palce_id = getattr(new, "place_id")
        user_id = getattr(new, "user_id")
        text = getattr(new, "text")
        self.assertTrue("place_id" in new.__dir__())
        self.assertTrue("user_id" in new.__dir__())
        self.assertTrue("text" in new.__dir__())
