import unittest

import pydj.di.utils as utils


class TestUtils(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(utils.add_two_numbers(3, 5), 8)
