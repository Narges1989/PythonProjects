import pytest

from src.py103.guide3 import guide3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide3:
    test_cases = [
        TestCase(given=1, expected=False),
        TestCase(given=17, expected=False),
        TestCase(given=2, expected=False),
        TestCase(given=-10, expected=False),
        TestCase(given=18, expected=True),
        TestCase(given=19, expected=True),
        TestCase(given=30, expected=True),
        TestCase(given=100, expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        age = test_case.given

        assert_equals(
            message=f"> age = {age}",
            expected=test_case.expected,
            actual=guide3(age=age),
        )
