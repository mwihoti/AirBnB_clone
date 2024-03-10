#!/usr/bin/python3
"""
Defines state test
"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """
    class TestState
    """

    def test_state_model_inheritance(self):
        """
        Test that state class inherits from BaseModel
        """

        new = State()
        self.assertIsInstance(new, BaseModel)

    def test_state_attr(self):
        """
        Test if state has name attribute
        """
        new = State()
        self.assertTrue("name" in new.__dir__())

    def test_state_str(self):
        """
        Check if attr is a string
        """
        new = State()
        nm_str = getattr(new, "name")
        self.assertIsInstance(nm_str, str)


if __name__ == '__main__':
    unittest.main()
