import unittest

from pydj.utils.common_utils import CommonUtils


class TestCommUtils(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.test_object = CommonUtils()

    def test_add_two_numbers(self):
        self.assertEqual(self.test_object.add_two_numbers(3, 5), 8)
