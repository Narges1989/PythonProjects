import pytest

from src.py104.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        TestCase(given=[1, 2, 3, 4], expected=[2, 3, 4]),
        TestCase(given=[4, 3, 2, 1], expected=[2, 3, 4]),
        TestCase(given=[2, 1, 3, 4], expected=[2, 3, 4]),
        TestCase(given=[-1, -2, -3, -4], expected=[-3, -2, -1]),
        TestCase(given=[-2, -3, -1, -4], expected=[-3, -2, -1]),
        TestCase(given=[-2, -3, 1, -4], expected=[-3, -2, 1]),
        TestCase(given=[1, 1, 1, 1], expected=[1]),
        TestCase(given=[-2, -2, -2], expected=[-2]),
        TestCase(given=[1, 2, 3, 4, 1, 2, 3, 4], expected=[2, 3, 4]),
        TestCase(given=[4, 3, 2, 1, 4, 3, 2, 1], expected=[2, 3, 4]),
        TestCase(given=[2, 1, 3, 4, 2, 1, 3, 4], expected=[2, 3, 4]),
        TestCase(given=[2, 2, 1], expected=[1, 2]),
        TestCase(given=[-10, 9, 13], expected=[-10, 9, 13]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task8(test_case.given),
        )
