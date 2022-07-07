#!/usr/bin/python3
"""
class my_list with a text file
"""


class Mylist(list):
    """
        This class inherits from list.
        Attributes:
        Methods:
            print_sorted - prints the list in ascending order
    """
    def print_sorted(self):
        """
            prints a list in ascending order.
        """
        print(sorted(self))
