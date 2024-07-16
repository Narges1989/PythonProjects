import pytest

from src.py103.guide18 import guide18
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide18:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1=1, given2=5, expected=5),
        TestCase2(given1=15, given2=25, expected=7500),
        TestCase2(given1=1, given2=4, expected=1),
        TestCase2(given1=2, given2=10, expected=50),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=test_case.expected,
            actual=guide18(a=a, b=b),
        )
