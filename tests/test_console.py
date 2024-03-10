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

    def test_create(self):
        """Creates an  instance """
        return HBNBCommand()
