import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])

    def test_boolean_in_list(self):
        self.assertEqual(max_integer([True, False, 2]), 2)
