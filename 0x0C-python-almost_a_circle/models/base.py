#!/usr/bin/python3
"""Creating base class"""


class Base:
    """Setting attributes for base class"""
    __nb_objects = 0

    def __init__(self, id = None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects ++
            self.id = Base.__nb_objects
