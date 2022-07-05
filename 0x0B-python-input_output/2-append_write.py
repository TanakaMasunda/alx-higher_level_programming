#!/usr/bin/python3
"""
function 2 write a string to a text file,returns e numbr of characters written
"""


def append_write(filename="", text=""):
    """function that appends and writes to afile
        Args:
            filename: filename
            text: text to be written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
