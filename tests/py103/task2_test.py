import pytest

from src.py103.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        TestCase(given=2, expected=True),
        TestCase(given=3, expected=True),
        TestCase(given=5, expected=True),
        TestCase(given=607, expected=True),
        TestCase(given=941, expected=True),
        TestCase(given=947, expected=True),
        TestCase(given=-90, expected=False),
        TestCase(given=0, expected=False),
        TestCase(given=1, expected=False),
        TestCase(given=4, expected=False),
        TestCase(given=39, expected=False),
        TestCase(given=51, expected=False),
        TestCase(given=66, expected=False),
        TestCase(given=70, expected=False),
        TestCase(given=150, expected=False),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> number= {test_case.given}",
            expected=test_case.expected,
            actual=task2(test_case.given),
        )
