#!/usr/bin/python3
"""
This module defines a 'Base' class for managing unique IDs for instances.

Usage:
    To use this module, create instances of the 'Base' class. Each instance
    will be assigned a unique ID.

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
        """
        Serialize a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries to be serialized.

        Returns:
            str: A JSON-formatted string representing the input list of
            dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            cls: The class calling the method (can be used to determine the
            filename).
            list_objs (list): A list of objects to be saved to a JSON file.

        Example:
            objects_list = [base_instance1, base_instance2]
            json_data = Base.to_json_string(objects_list)

            Base.save_to_file(objects_list)  # Saves objects_list to a JSON
            file.
        """
        # Define the file name based on the class name
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                jstr = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(jstr))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation into a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A list of dictionaries representing the JSON data.

        Note:
            If the input JSON string is empty or "{}", an empty list is
            returned.
        """
        if json_string is None or json_string == "{}":
            return []

        return json.loads(json_string)
