#!/usr/bin/python3
"""write a function that returns the JSON representation of an object (string)
"""
import json


def from_json_string(my_str):
    """function that returns the JSON representation of an object
        Args:
            my_str: object

        Raises:
             exception: when rhe object cant be encoded
    """
    return json.loads(my_str)
