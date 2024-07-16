import pytest

from src.py103.guide11 import guide11
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase3


class TestGuide11:
    test_cases = [
        # given1 is a, given2 is b, given3 is c
        TestCase3(given1=30, given2=30, given3=30, expected="equilateral"),
        TestCase3(given1=61, given2=61, given3=61, expected="equilateral"),
        TestCase3(given1=55, given2=55, given3=55, expected="equilateral"),
        TestCase3(given1=11, given2=11, given3=19, expected="isosceles"),
        TestCase3(given1=8, given2=29, given3=29, expected="isosceles"),
        TestCase3(given1=18, given2=47, given3=47, expected="isosceles"),
        TestCase3(given1=31, given2=55, given3=40, expected="scalane"),
        TestCase3(given1=21, given2=68, given3=49, expected="scalane"),
        TestCase3(given1=11, given2=23, given3=19, expected="scalane"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2
        c = test_case.given3

        assert_equals(
            message=f"> a = {a}\n> b = {b}\n> c = {c}",
            expected=test_case.expected,
            actual=guide11(a=a, b=b, c=c),
        )
