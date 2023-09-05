#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unittest class  for max_integer """
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_module_doctring(self):
        """ Tests for module docstring """
        m_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(m_doc) > 1)

    def test_function_docstring(self):
        """ Tests for function docstring """
        f_doc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(f_doc) > 1)

    def test_positive_and_negaive_integers(self):
        """
        Tests max_integer with a list of positive, negative and mixed integers
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    def test_one_element(self):
        """
        Tests max integer with list containing one element
        """
        result = max_integer([45])
        self.assertEqual(result, 45)

        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)

    def test_empty_list(self):
        """
        Test max_integer with an empty list
        """
        empty_list = max_integer()
        self.assertIsNone(empty_list)

    def test_wrong_list_type(self):
        """
        Test max_integer with incorrect input types
        """
        with self.assertRaises(TypeError):
            self.wrong_type = max_integer("Not a list")
            self.wrong_type = max_integer((1, 2, 3, 4))
            self.wrong_type = max_integer({1, 2, 3, 4})
            self.wrong_type = max_integer({'First': 1, 'Second': 2})
            self.wrong_type = max_integer()

    def test_wrong_variable_type(self):
        """
        Test max_integer with lists containing elements of incorrect types
        """
        with self.assertRaises(TypeError):
            self.wrong_type_in_list = max_integer([1, 2, "Sarah", 4])
            self.wrong_type_in_list = max_integer([1, 2, True, 4])

    def test_integers_and_floats(self):
        """
        Test max_integer with lists containing integers and floats
        """
        result = max_integer([1.2, 2, 3.1, 4, 4.5])
        self.assertEqual(result, 4.5)

        result = max_integer([1.2, 2.4, 3.1, 4.9, 4.5])
        self.assertEqual(result, 4.9)


if __name__ == "__main__":
    unittest.main()
