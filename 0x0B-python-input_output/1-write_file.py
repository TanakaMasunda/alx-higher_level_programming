#!/usr/bin/python3
"""
function 2 write a string to a text file,returns e numbr of characters written
"""


def write_file(filename="", text=""):
    """function that writes to afile
        Args:
            filename: filename
            text: text to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
