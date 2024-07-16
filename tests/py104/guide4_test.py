import pytest

from src.py104.guide4 import guide4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide4:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1=50, given2=10, expected=[]),
        TestCase2(given1=25, given2=25, expected=[]),
        TestCase2(given1=20, given2=20, expected=[]),
        TestCase2(given1=5, given2=10, expected=[25, 7, 9]),
        TestCase2(given1=10, given2=15, expected=[11, 13, 225]),
        TestCase2(given1=1, given2=10, expected=[1, 3, 25, 7, 9]),
        TestCase2(given1=33, given2=40, expected=[33, 1225, 37, 39]),
        TestCase2(given1=3, given2=4, expected=[3]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=sorted(test_case.expected),
            actual=sorted(guide4(a=a, b=b)),
        )
