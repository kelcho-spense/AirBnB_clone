#!/usr/bin/python3
"""
File: review.py



Defines a class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a Review inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
