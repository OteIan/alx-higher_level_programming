#!/usr/bin/python3
"""
Unit tests for the 'Square' class in the 'models.square' module.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import models.square as sq
from models.square import Square


class TestSquareCLass(unittest.TestCase):
    """ Test cases for 'Square' class' """
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_module_docstring(self):
        """ Tests for module docstring """
        m_doc = sq.__doc__
        self.assertIsNotNone(m_doc)

    def test_class_docstring(self):
        """ Tests for class docstring """
        c_doc = Square.__doc__
        self.assertIsNotNone(c_doc)

    def test_function_docstring(self):
        """ Tests for function docstring """
        f_doc = Square.__init__.__doc__
        self.assertIsNotNone(f_doc)

    def test_unique_id(self):
        """ Tests that the id of an instance is unique to the others """
        s1 = Square(2, id=6)
        s2 = Square(2, id=567)
        s3 = Square(2, id=12)
        s4 = Square(8, id=65)

        self.assertNotEqual(s1, s2)
        self.assertNotEqual(s1, s3)
        self.assertNotEqual(s1, s4)
        self.assertNotEqual(s2, s3)
        self.assertNotEqual(s2, s4)
        self.assertNotEqual(s3, s4)

    def test_square_id(self):
        """ Tests for the id """
        s1 = Square(2, id=6)
        self.assertEqual(s1.id, 6)

        s2 = Square(10, id=567)
        self.assertEqual(s2.id, 567)

        s3 = Square(100, id=12)
        self.assertEqual(s3.id, 12)

    def test_wrong_types_and_values(self):
        """ Tests for wrong input types """
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"
            s.size = [8, 9]
            s.size = {98, 4}
            s.size = (47, 2)

        with self.assertRaises(ValueError):
            s.size = 0
            s.size = -9

    def test_area(self):
        """ Tests for the area of the square """
        s1 = Square(10)
        s2 = Square(3)
        s3 = Square(147)
        s4 = Square(98)

        self.assertEqual(s1.area(), 100)
        self.assertEqual(s2.area(), 9)
        self.assertEqual(s3.area(), 21609)
        self.assertEqual(s4.area(), 9604)

    def test_display_output_without_coordinates(self):
        """ Tests the output of the square display function """

        # Test without (x) and (y)
        s1 = Square(3)
        expected_output = "###\n###\n###\n"

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            s1.display()
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_display_output_with_coordinates(self):
        # Test with (x) and (y)
        s2 = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            s2.display()
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, expected_output)


    def test_return(self):
        """ Tests the return value held when Square() is called"""
        s = Square(12, 4, 2, 908)

        with patch("sys.stdout", new_callable=StringIO) as mock_output:
            print(s)
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, "[Square] (908) 4/2 - 12\n") 

    def test_update_function(self):
        """ This tests whether the Square updates when updated """
        s = Square(10, 10, 10, 10)
        s.update(908, 12, 4, 2)

        with patch("sys.stdout", new_callable=StringIO) as mock_output:    
            print(s)
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, "[Square] (908) 4/2 - 12\n")

    def test_update_keyword_function(self):
        """ This tests whether the square updates when updated with keywords
        """
        s = Square(10, 10, 10, 10)
        s.update(size=12, x=4, y=2, id=908)

        with patch("sys.stdout", new_callable=StringIO) as mock_output:    
            print(s)
            actual_output = mock_output.getvalue()

        self.assertEqual(actual_output, "[Square] (908) 4/2 - 12\n")

    def test_convert_to_dict(self):
        """ Tests whether the Square has been correctly represented as
        a dictionary """
        s = Square(7, 4, 1, 3)
        s_dict = s.to_dictionary()
        expected_output = {
            'id': 3,
            'size': 7,
            'x': 4,
            'y': 1
        }

        self.assertDictEqual(s_dict, expected_output)



if __name__ == "__main__":
    unittest.main()