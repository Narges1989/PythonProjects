import pytest

from src.py102.guide5 import guide5
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase3


class TestGuide5:
    test_cases = [
        # given1 is a, given2 is b, given3 is c
        TestCase3(given1=5.0, given2=15.0, given3=11.0, expected=31.0),
        TestCase3(given1=0.0, given2=0.0, given3=0.0, expected=0.0),
        TestCase3(given1=5.0, given2=9.0, given3=11.0, expected=25.0),
        TestCase3(given1=51.0, given2=91.0, given3=111.0, expected=253.0),
        TestCase3(given1=21.0, given2=78.0, given3=80.0, expected=179),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2
        c = test_case.given3

        assert_almost_equals(
            message=f"> a = {a}\n> b = {b}\n> c = {c}",
            expected=test_case.expected,
            actual=guide5(a=a, b=b, c=c),
        )
