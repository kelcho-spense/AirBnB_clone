#!/usr/bin/python3
"""
File: city.py



Defines a class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a City inheriting from BaseModel"""
    state_id = ""
    name = ""
