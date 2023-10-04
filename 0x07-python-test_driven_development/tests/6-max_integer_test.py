#!/usr/bin/python3
"""Unittests for max_integer. """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer. """

    def test_arranged_list(self):
        """Test an ordered list of integers."""
        arranged = [1, 2, 3, 4]
        self.assertEqual(max_integer(arranged), 4)

    def test_unarranged_list(self):
        """Test an unordered list of integers."""
        unarranged = [1, 2, 4, 3]
        self.assertEqual(max_integer(unarranged), 4)

    def test_max_at_start(self):
        """Test a list with a beginning max value."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element = [7]
        self.assertEqual(max_integer(single_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Melvin"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Melvin", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
