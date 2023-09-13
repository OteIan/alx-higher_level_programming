#!/usr/bin/python3
"""
This script defines a 'Student' class for representing student information.

Usage:
    To use this script, create an instance of the 'Student' class and utilize
    the 'to_json' method to convert student data to a JSON-compatible
    dictionary

Example:
    from student_module import Student

    # Create a Student instance
    student = Student("John", "Doe", 20)

    # Convert the Student instance to a JSON dictionary with all attributes
    json_data = student.to_json()

    # Convert the Student instance to a JSON dictionary with selected
    attributes
    selected_attrs = ["first_name", "age"]
    json_data = student.to_json(selected_attrs)
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
