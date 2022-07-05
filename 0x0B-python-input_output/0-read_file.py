#!/usr/bin/python3
"""
Read a text file using with and no import
"""


def read_file(filename=""):
    """function that reads from sa text file
        Args
            filename: filename
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
