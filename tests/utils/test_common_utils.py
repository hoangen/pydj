import unittest

from pydj.utils import CommonUtils


class TestCommUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(CommonUtils.add(3, 5), 8)

    def test_multiply(self):
        self.assertEqual(CommonUtils.multiply(3, 5), 15)
