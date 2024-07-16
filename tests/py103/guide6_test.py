import pytest

from src.py103.guide6 import guide6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase

test_cases = [
    TestCase(given=0, expected="infant"),
    TestCase(given=1, expected="infant"),
    TestCase(given=2, expected="toddler"),
    TestCase(given=3, expected="toddler"),
    TestCase(given=4, expected="toddler"),
    TestCase(given=5, expected="child"),
    TestCase(given=8, expected="child"),
    TestCase(given=12, expected="child"),
    TestCase(given=13, expected="teen"),
    TestCase(given=15, expected="teen"),
    TestCase(given=19, expected="teen"),
    TestCase(given=20, expected="adult"),
    TestCase(given=25, expected="adult"),
    TestCase(given=39, expected="adult"),
    TestCase(given=40, expected="middle adult"),
    TestCase(given=50, expected="middle adult"),
    TestCase(given=59, expected="middle adult"),
    TestCase(given=60, expected="senior adult"),
    TestCase(given=61, expected="senior adult"),
    TestCase(given=70, expected="senior adult"),
    TestCase(given=77, expected="senior adult"),
]


class TestGuide6:
    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        age = test_case.given

        assert_equals(
            message=f"> age = {age}",
            expected=test_case.expected,
            actual=guide6(age=age),
        )
