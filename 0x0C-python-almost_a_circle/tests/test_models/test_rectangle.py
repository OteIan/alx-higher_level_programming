#!/usr/bin/python3
"""  """
import unittest
from unittest.mock import patch
from io import StringIO
import models.rectangle as rect
from models.rectangle import Rectangle
import json


class TestRectangleClass(unittest.TestCase):
    """  """
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_module_docstring(self):
        """ Tests for module docstring """
        m_doc = rect.__doc__
        self.assertIsNotNone(m_doc)

    def test_class_docstring(self):
        """ Tests for class docstring """
        c_doc = Rectangle.__doc__
        self.assertIsNotNone(c_doc)

    def test_function_docstring(self):
        """ Tests for function docstring """
        f_doc = Rectangle.__init__.__doc__
        self.assertIsNotNone(f_doc)

    def test_unique_id(self):
        """ Tests that the id of an instance is unique to the others """
        r1 = Rectangle(10, 2, id=6)
        r2 = Rectangle(2, 10, id=567)
        r3 = Rectangle(10, 2, id=12)
        r4 = Rectangle(78, 8, id=65)

        self.assertNotEqual(r1, r2)
        self.assertNotEqual(r1, r3)
        self.assertNotEqual(r1, r4)
        self.assertNotEqual(r2, r3)
        self.assertNotEqual(r2, r4)
        self.assertNotEqual(r3, r4)

    def test_rectangle_id(self):
        """ Tests for the id """
        r1 = Rectangle(10, 2, id=6)
        self.assertEqual(r1.id, 6)

        r2 = Rectangle(2, 10, id=567)
        self.assertEqual(r2.id, 567)

        r3 = Rectangle(10, 2, id=12)
        self.assertEqual(r3.id, 12)

    def test_wrong_types_and_values(self):
        """ Tests for wrong input types """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
            Rectangle("2", 10)
            Rectangle(10, 2, "not an int")
            Rectangle(10, 2, 1, {1, "Not an int"})
            Rectangle(True, 7, 9)
            Rectangle((14, 3), {9, 0}, "Not an int", [137, 8])
            Rectangle(10.2, 2)
            Rectangle(10, 2.3)

        with self.assertRaises(ValueError):
            Rectangle(0, 1)
            Rectangle(1, 0)
            Rectangle(-1, 1)
            Rectangle(1, -1)
            Rectangle(-1, 0)
            Rectangle(0, 0)
            Rectangle(-2, -2)
            Rectangle(2, 2, -3, 0)
            Rectangle(2, 2, 8, -7)
            Rectangle(2, 2, -4, -4)

    def test_area(self):
        """ Tests for the area of the rectangle """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(3, 9)
        r3 = Rectangle(14, 7)
        r4 = Rectangle(98, 705)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 27)
        self.assertEqual(r3.area(), 98)
        self.assertEqual(r4.area(), 69090)

    def test_display_output_without_coordinates(self):
        """ Tests the output of the rectangle display function """

        # Test without (x) and (y)
        r1 = Rectangle(10, 2)
        expected_output = "##########\n##########\n"

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            r1.display()
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_display_output_with_coordinates(self):
        # Test with (x) and (y)
        r2 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            r2.display()
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_return(self):
        """ Tests the return value held when Rectangle() is called"""
        r = Rectangle(12, 3, 4, 2, 908)

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            print(r)
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, "[Rectangle] (908) 4/2 - 12/3\n")

    def test_update_function(self):
        """ This tests whether the rectangle updates when updated """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(908, 12, 3, 4, 2)

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            print(r)
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, "[Rectangle] (908) 4/2 - 12/3\n")

    def test_update_keyword_function(self):
        """ This tests whether the rectangle updates when updated with keywords
        """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=3, width=12, x=4, y=2, id=908)

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            print(r)
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, "[Rectangle] (908) 4/2 - 12/3\n")

    def test_convert_to_dict(self):
        """ Tests whether the Rectangle has been correctly represented as
        a dictionary """
        r = Rectangle(10, 2, 4, 3, 1)
        r_dict = r.to_dictionary()
        expected_output = {
            'id': 1,
            'width': 10,
            'height': 2,
            'x': 4,
            'y': 3
        }

        self.assertDictEqual(r_dict, expected_output)

    def test_sace_to_file_with_objects(self):
        """ Test saving objects to a JSON file """
        r1 = Rectangle(11, 5, 2, 3, 3)
        r2 = Rectangle(1, 3, id=7)
        Rectangles = [r1, r2]

        Rectangle.save_to_file(Rectangles)

        expected_output = [
            r1.to_dictionary(),
            r2.to_dictionary()
        ]

        with open("Rectangle.json", "r") as file:
            file_content = json.load(file)

        self.assertEqual(file_content, expected_output)

    def test_save_to_file_with_None(self):
        """ Test saving an empty list when list_obj is None """
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            file_content = json.load(file)

        self.assertEqual(file_content, [])


if __name__ == "__main__":
    unittest.main()
