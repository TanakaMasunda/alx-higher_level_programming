#!/usr/bin/python3
"""class base geometry"""


class BaseGeometry:
    """
    base geometry
    Attributes: None
    Method:
        area(): raises an exception
        integer_validator: validates value
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator checks the value
        Args:
            name(str): name
            value(int): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
