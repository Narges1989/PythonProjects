import pytest

from src.py103.guide14 import guide14
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide14:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1=10, given2=5, expected=-1),
        TestCase2(given1=0, given2=-17, expected=-1),
        TestCase2(given1=3, given2=3, expected=-1),
        TestCase2(given1=11, given2=13, expected=12),
        TestCase2(given1=1, given2=5, expected=6),
        TestCase2(given1=4, given2=5, expected=4),
        TestCase2(given1=100, given2=110, expected=630),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=test_case.expected,
            actual=guide14(a=a, b=b),
        )
