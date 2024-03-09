#!/usr/bin/env python3
"""
Defines Review class Model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    defines class Review
    """
    place_id = ""
    user_id = ""
    text = ""
