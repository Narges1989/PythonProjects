import pytest

from src.py104.task3 import task3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[1, 2, 3, 4], expected=[]),
        TestCase(given=[1, 1, 1, 2, 2, 3], expected=[1, 2]),
        TestCase(given=[5, 6, 5, 6, 7, 8, 7], expected=[5, 6, 7]),
        TestCase(given=[0, 0, 0, 0], expected=[0]),
        TestCase(given=[-1, -1, 0, -2, -2], expected=[-1, -2]),
        TestCase(given=[-9, -9, 9, 1, 1, -9, 9, 3, 2, 2], expected=[-9, 9, 1, 2]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=sorted(test_case.expected),
            actual=sorted(task3(test_case.given)),
        )
