import pytest

from src.py104.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask5:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[67], expected=[0]),
        TestCase(given=[5, 6, 7, 10, 19], expected=[0, 6, 14, 30, 76]),
        TestCase(given=[1, 2, 3], expected=[0, 2, 6]),
        TestCase(given=[0, 0, 0], expected=[0, 0, 0]),
        TestCase(given=[0, -1, -2, -3], expected=[0, -1, -4, -9]),
        TestCase(given=[0, -1, -2, -1], expected=[0, -1, -4, -3]),
        TestCase(
            given=[5, 7, 3, 5, 2, 10, 9, 78, 5, 17],
            expected=[0, 7, 6, 15, 8, 50, 54, 546, 40, 153],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task5(test_case.given),
        )
