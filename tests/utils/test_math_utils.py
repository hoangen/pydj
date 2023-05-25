import unittest

import pydj.utils.math_utils as math_utils


class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_utils.add(3, 5), 8)

    def test_multiply(self):
        self.assertEqual(math_utils.multiply(3, 5), 15)
