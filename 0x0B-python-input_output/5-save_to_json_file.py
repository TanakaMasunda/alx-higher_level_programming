#!/usr/bin/python3
"""write a function that returns the JSON representation of an object (string)
"""
import json


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object
        Args:
            my_obj: object
            filename: text filename

        Raises:
             exception: when rhe object cant be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
