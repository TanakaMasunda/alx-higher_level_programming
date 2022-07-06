#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """is same class returns true  object is exactly  of the same instance
        Args:
            obj(object): object being checked
            a_class(class: class
        Return: boolean(True or False)
    """
    if type(obj) is a_class:
        return True
    else:
        return False
