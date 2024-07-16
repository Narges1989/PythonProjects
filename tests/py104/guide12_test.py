import pytest

from src.py104.guide12 import guide12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide12:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1=5, given2=16, expected=[6, 7, 8, 9, 50, 11, 12, 13, 14, 45]),
        TestCase2(given1=5, given2=15, expected=[6, 7, 8, 9, 50, 11, 12, 13, 14]),
        TestCase2(given1=4, given2=11, expected=[15, 6, 7, 8, 9, 50]),
        TestCase2(given1=10, given2=20, expected=[11, 12, 13, 14, 45, 16, 17, 18, 19]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=sorted(test_case.expected),
            actual=sorted(guide12(a=a, b=b)),
        )
