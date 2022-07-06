#!/usr/bin/python3
"""class Rectangle from BaseGeomerty """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle inherits from BaseGeometry
        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle
            Methods:
                __init__ - initialisation of the Rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
