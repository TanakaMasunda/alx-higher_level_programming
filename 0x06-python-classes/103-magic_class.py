#!/usr/bin/python3
"""Class Magicclass"""
import math


class MagicClass:
    """Defines MagicClass"""
    def __init__(self, radius=0):
        """initializes the data"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius is not a number")
        self.__radius = radius

    def area(self):
        """get the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """get the circumference"""
        return (2 * math.pi * self.__radius)
