#!/usr/bin/env python3
""" Defines user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
