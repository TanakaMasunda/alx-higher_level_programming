#!/usr/bin/python3
"""Write a class Student that defines a student by age, first and last name
"""


class Student:
    """representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize new student in class

        Args:
            first_name(string) is the first name of the student
            last_name(string) is the last name of the student
            age(integer) is the age of the student
        """
        self.first_name = first name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
