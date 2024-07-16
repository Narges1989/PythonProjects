import pytest

from src.py104.guide19 import guide19
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide19:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1=6, given2=18, expected=(9, 15)),
        TestCase2(given1=3, given2=9, expected=(3, 9)),
        TestCase2(given1=3, given2=16, expected=(3, 9, 15)),
        TestCase2(given1=20, given2=22, expected=(21,)),
        TestCase2(given1=30, given2=39, expected=(33, 39)),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=(test_case.expected),
            actual=(guide19(a=a, b=b)),
        )
