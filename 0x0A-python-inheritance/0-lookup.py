#!/usr/bin/python3
"""function that return list of available attributes,methods of an object"""


def lookup(obj):
    """returns list list of available attributes"""
    return(dir(obj))
