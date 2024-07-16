import pytest

from src.py103.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        TestCase(given=0, expected=0),
        TestCase(given=2, expected=2),
        TestCase(given=100, expected=1),
        TestCase(given=1000, expected=1),
        TestCase(given=123, expected=6),
        TestCase(given=675, expected=18),
        TestCase(given=847, expected=19),
        TestCase(given=726, expected=15),
        TestCase(given=895, expected=22),
        TestCase(given=187263, expected=27),
        TestCase(given=87223, expected=22),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> number= {test_case.given}",
            expected=test_case.expected,
            actual=task8(test_case.given),
        )
