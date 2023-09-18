#!/usr/bin/python3
""" Unittest for Base """
import unittest
import models.base as one
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Unittest class for base """
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_module_docstring(self):
        """ Tests for module docstring """
        m_doc = one.__doc__
        self.assertIsNotNone(m_doc)

    def test_class_docstring(self):
        """ Tests for class docstring """
        c_doc = Base.__doc__
        self.assertIsNotNone(c_doc)

    def test_function_docstring(self):
        """ Tests for function docstring """
        f_doc = Base.__init__.__doc__
        self.assertIsNotNone(f_doc)

    def test_base_class(self):
        """ Test the base class """
        b1 = Base(12)
        b2 = Base(0)
        b3 = Base(9)

        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 0)
        self.assertEqual(b3.id, 9)

    def test_unique_id(self):
        """ Tests that the id of an instance is unique to the others """
        b1 = Base(12)
        b2 = Base(0)
        b3 = Base(9)
        b4 = Base(809323)

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b4.id)
        self.assertNotEqual(b2.id, b4.id)
        self.assertNotEqual(b3.id, b4.id)

    def test_dict_to_json_string(self):
        """ Tests if the dictionary is correctly represented in string format
        """
        list_dict = {"x": 3, "width": 11, "id": 5, "height": 6, "y": 4}
        expected_output = '{"x": 3, "width": 11, "id": 5, "height": 6, "y": 4}'

        json_string = Base.to_json_string(list_dict)

        self.assertEqual(json_string, expected_output)

        list_dict = {}
        expected_output = []

        json_string = Base.to_json_string(list_dict)

        self.assertEqual(json_string, expected_output)


if __name__ == "__main__":
    unittest.main()
