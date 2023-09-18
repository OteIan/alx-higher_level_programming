#!/usr/bin/python3
"""
This module defines a 'Base' class for managing unique IDs for instances.

Usage:
    To use this module, create instances of the 'Base' class. Each instance will
    be assigned a unique ID.

Example:
    base_instance1 = Base()
    print(base_instance1.id)  # Outputs a unique ID (1)
    base_instance2 = Base()
    print(base_instance2.id)  # Outputs a unique ID (2)
"""
import json


class Base:
    """
    A class for managing unique IDs for instances.

    Class Attributes:
        __nb_objects (int): A counter to keep track of the number of instances.

    Attributes:
        id (int): A unique ID assigned to each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): An optional ID to assign to the instance.
                If not provided, a unique ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """  """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """  """
        if list_objs is None:
            list_objs = []
            
        # Define the file name based on the class name
        filename = cls.__name__ + ".json"

        # Convert list_objs to a JSON string
        json_str = cls.to_json_string(list_objs)

        # Write JSON string to file, overwrite if it exists
        with open(filename, "w") as file:
            file.write(json_str)
