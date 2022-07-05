#!/usr/bin/python3
"""write a function that returns the JSON representation of an object (string)
"""
import json


def load_from_json_file(filename):
    """function that returns the JSON representation of an object
        Args:
            my_obj: object
            filename: text filename

        Raises:
             exception: when rhe object cant be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
