#!/usr/bin/python3
"""
This script defines a class 'Student' with methods for initializing and
converting a student object to a JSON-compatible dictionary.

Usage:
    To use this script, create an instance of the 'Student' class and use the
    'to_json' method to convert it to a dictionary.

Example:
    student = Student("John", "Doe", 20)
    student_data = student.to_json()
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

    def to_json(self):
        """
        Convert the Student object to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary containing the attributes of the Student object
        """
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

        return data
