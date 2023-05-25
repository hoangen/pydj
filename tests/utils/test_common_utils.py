import unittest

from pydj.utils.common_utils import CommonUtils


class TestCommUtils(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.test_obj = CommonUtils()

    def test_add(self):
        self.assertEqual(self.test_obj.add(3, 5), 8)

    def test_multiply(self):
        self.assertEqual(CommonUtils.multiply(3, 5), 15)
