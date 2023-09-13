#!/usr/bin/python3
"""
This module defines a 'Student' class for representing student information
and includes methods to convert a 'Student' object to a JSON-compatible
dictionary and to update a 'Student' object's attributes from a JSON
dictionary.
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object to a JSON-compatible dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include in
            the JSON dictionary.
                If None, include all attributes (first name, last name, age)

        Returns:
            dict: A dictionary containing the specified attributes of the
            Student object.
        """
        data = {}

        if attrs is None:
            data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            for name in attrs:
                try:
                    value = getattr(self, name)
                    data[name] = value
                except AttributeError:
                    pass

        return data

    def reload_from_json(self, json):
        """
        Update a Student object's attributes from a JSON dictionary.

        Args:
            json (dict): A JSON dictionary containing attribute names and
            values.

        Returns:
            self: The updated Student object.
        """
        for key, value in json.items():
            setattr(self, key, value)
