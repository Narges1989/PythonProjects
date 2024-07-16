import pytest

from src.py103.guide10 import guide10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase3


class TestGuide10:
    test_cases = [
        # given1 is a, given2 is b, given3 is c
        TestCase3(given1=7, given2=10, given3=5, expected=True),
        TestCase3(given1=30, given2=30, given3=30, expected=True),
        TestCase3(given1=10, given2=22, given3=18, expected=True),
        TestCase3(given1=10, given2=220, given3=18, expected=False),
        TestCase3(given1=11, given2=29, given3=56, expected=False),
        TestCase3(given1=19, given2=120, given3=80, expected=False),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2
        c = test_case.given3

        assert_equals(
            message=f"> a = {a}\n> b = {b}\n> c = {c}",
            expected=test_case.expected,
            actual=guide10(a=a, b=b, c=c),
        )
