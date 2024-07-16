import pytest

from src.py106.task1 import task1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask1:
    test_cases = [
        TestCase(given="Gothenburg", expected=10),
        TestCase(given="ABCD ABCD", expected=9),
        TestCase(given=None, expected=0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task1(test_case.given),
        )
