import pytest

from src.py104.guide20 import guide20
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide20:
    test_cases = [
        TestCase2(
            given1={10, 100, 20, 900, 800, 777, 30},
            given2={50, 40, 30, 14, 20},
            expected={20, 30},
        ),
        TestCase2(given1={1, 3, 5, 7, 8}, given2={7, 8, 9, 3}, expected={3, 7, 8}),
        TestCase2(given1={1, 2, 3}, given2={4, 5, 6}, expected=set()),
        TestCase2(given1={}, given2={}, expected=set()),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=test_case.expected,
            actual=guide20(a=a, b=b),
        )
