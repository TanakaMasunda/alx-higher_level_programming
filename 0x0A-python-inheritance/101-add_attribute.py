#!/usr/bin/python3
"""add attribute"""


def add_attribute(cls, name, value):
    """
        add new attributes when possible
    """
    if hasattr(cls, '__dict__'):
        setattr(cls, name, value)
    else:
        raise TypeError("cant add new attribute")
