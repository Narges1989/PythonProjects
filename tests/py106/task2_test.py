import pytest

from src.py106.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        TestCase(given=[-1, -2, -3], expected=0),
        TestCase(given=[1, 2, 3], expected=0),
        TestCase(given=[], expected=0),
        TestCase(given=None, expected=0),
        TestCase(given=[-1, None, -3], expected=1),
        TestCase(given=[1, 2, 3, None, None], expected=2),
        TestCase(given=[None, 1, None, 3, None], expected=3),
        TestCase(given=[None, -1, -2, 3, None, None, None], expected=4),
        TestCase(given=[None, None, None, None, None], expected=5),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task2(test_case.given),
        )
