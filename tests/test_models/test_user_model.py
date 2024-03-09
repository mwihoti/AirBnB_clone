#!/usr/bin/python3

"""
Defines Test_user for USer model
"""


import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime

class TestUser(unittest.TestCase):
    """
    Defines class TestUser
    """

    def test_user_model(self):
        """
        tests that the User class Inherits from BaseModel
        """
        new_usr = User()
        self.assertIsInstance(new_usr, BaseModel)

    def test_user_attr(self):
        """
        Tests users attributes
        """

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_str_email(self):
        """
        Tests if email is string
        """
        new = User()
        em = getattr(new, "email")
        self.assertIsInstance(em, str)
