#!/usr/bin/python3
"""is kind of class returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """is same class returns true  object is exactly  of the same instance
        Args:
            obj(object): object
            a_classclass: class
        Return: boolean(True or False)
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
