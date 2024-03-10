#!/usr/bin/env python3
"""
Defines Test for console.py
"""

import unittest
import console
from console import HBNBCommand


class testConsole(unittest.TestCase):
    """
    Defines class testConsole
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
