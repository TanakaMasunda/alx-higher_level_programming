#!/usr/bin/python3
"""Write a function that returns True if the object is an instance of a class,
that inherited (directly/indirectly) from the specified class,otherwise False
"""


def inherits_from(obj, a_class):
    """returns true  object inherits from the specified class
        Args:
            obj(object): object being checked
            a_class(class: class
        Return: boolean(True or False)
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
