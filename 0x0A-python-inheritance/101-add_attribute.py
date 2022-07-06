#!/usr/bin/python3
"""add attribute"""


def add_attribute(clas, name, value):
    """
        add new attributes when possible
    """
    if hasattr(clas, "__dict__") is False:
        raise TypeError("cant add new attribute")
    setattr(clas, name, value)
