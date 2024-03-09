import unittest
"""
Tests for class BaseModel
"""
import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Defines class TestBaseodel
    """

    def setUp(self):
        """
        initializes an instance of the BaseModel class and assigns
        a name attribute to it
        """
        self.my_model = BaseModel()
        self.my_model.name = "Dan Mwihoti"

    def tearDown(self):
        """
        Clearing instance
        """
        del self.my_model

    def test_instantiation(self):
        """
        Tests number of arguements instantiates
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_str(self):
        """
        checks if id is string
        """
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_updated_created_equal(self):
        """
            Checks if updated_at & created_at  dates are equal.
        """
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_save(self):
        """
            Checks whether after updating the instance; the dates differ in the
            updated_at attribute.
        """
        prev = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, prev)

    def test_dict_class(self):
        """
            Checks  __class__ name.
        """

        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_dict_updated(self):
        """
        Checks the data type of the updated_at value in the dictionary.
        """
        self.assertEqual("<class 'str'>",
                         str(type((self.my_model.to_dict())["updated_at"])))

    def test_dict_Type_created(self):
        """
        Checks the data type of the created_at value in the dictionary.
        """
        check = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(check["created_at"])))
