from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest

from src.task import my_sum
from test.test_logger import TestLogger


class TaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results()

    def test_should_sum_two_positive_values(self):
        a = 47
        b = 53
        result = my_sum(a, b)
        TaskTest.logger.log_single_test_result("should_sum_two_positive_values", result == 100)
        self.assertEqual(100, result)

    def test_should_sum_two_negative_values(self):
        a = -47
        b = -53
        result = my_sum(a, b)
        TaskTest.logger.log_single_test_result("should_sum_two_negative_values", result == -100)
        self.assertEqual(-100, result)

    def test_should_sum_two_decimal_values(self):
        a = 27.5487746
        b = 94.84745641
        result = my_sum(a, b)
        TaskTest.logger.log_single_test_result("should_sum_two_decimal_values", round(result, 2) == 122.40)
        self.assertEqual(122.40, round(result, 2))

    def test_should_sum_two_zero_values(self):
        a = 0
        b = 0
        result = my_sum(a, b)
        TaskTest.logger.log_single_test_result("should_sum_two_zero_values", result == 0)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
