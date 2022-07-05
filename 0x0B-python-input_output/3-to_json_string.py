#!/usr/bin/python3
"""write a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object
        Args:
            my_obj: object

        Raises:
             exception: when rhe object cant be encoded
    """
    return json.dumps(my_obj)
