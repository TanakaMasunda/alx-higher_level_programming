#!/usr/bin/python3
"""add attribute"""


def add_attribute(cls, name, value):
    """
        add new attributes when possible
    """
    if hasattr(cls, "__dict__") is False:
        raise TypeError("cant add new attribute")
    setattr(cls, name, value)
