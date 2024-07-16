import pytest

from src.py103.task1 import task1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask1:
    test_cases = [
        # given1 is a, given2 is b
        TestCase2(given1=1, given2=10, expected=55),
        TestCase2(given1=-1, given2=5, expected=14),
        TestCase2(given1=-10, given2=-3, expected=-52),
        TestCase2(given1=10, given2=1, expected=0),
        TestCase2(given1=18, given2=9, expected=0),
        TestCase2(given1=31, given2=20, expected=0),
        TestCase2(given1=1, given2=1, expected=0),
        TestCase2(given1=0, given2=0, expected=0),
        TestCase2(given1=-10, given2=-10, expected=0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a= {a}\n> b= {b}",
            expected=test_case.expected,
            actual=task1(a, b),
        )
