import pytest

from src.py106.task6 import task6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask6:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[None, None, None], expected=[None, None, None]),
        TestCase(given=[None, 1, 2, 3, None], expected=[None, 1, 4, 9, None]),
        TestCase(given=[1, 2, 3, 4, None], expected=[0, 2, 6, 12, None]),
        TestCase(given=[None, 1, 2, 3, 4, None], expected=[None, 1, 4, 9, 16, None]),
        TestCase(given=[1, 2, 3, 4], expected=[0, 2, 6, 12]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task6(test_case.given),
        )
