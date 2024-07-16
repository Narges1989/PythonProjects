import pytest

from src.py103.task3 import task3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        TestCase(given=0, expected=1),
        TestCase(given=1, expected=1),
        TestCase(given=2, expected=2),
        TestCase(given=3, expected=6),
        TestCase(given=4, expected=24),
        TestCase(given=5, expected=120),
        TestCase(given=6, expected=720),
        TestCase(given=7, expected=5040),
        TestCase(given=8, expected=40320),
        TestCase(given=9, expected=362880),
        TestCase(given=10, expected=3628800),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> number= {test_case.given}",
            expected=test_case.expected,
            actual=task3(test_case.given),
        )
