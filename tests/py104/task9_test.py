import pytest

from src.py104.task9 import task9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[5, 2, 3, 4], expected=[25, 10, 6, 12]),
        TestCase(given=[9, 1, 2, 3, 6], expected=[81, 9, 2, 6, 18]),
        TestCase(given=[4], expected=[16]),
        TestCase(given=[1, -2, 3, -4], expected=[1, -2, -6, -12]),
        TestCase(given=[1, 1, 1, 1], expected=[1, 1, 1, 1]),
        TestCase(given=[0, 1, 0, 1], expected=[0, 0, 0, 0]),
        TestCase(
            given=[-1, 0, 1, 2, 3, 4, 5, -9, -10, 0, 100],
            expected=[1, 0, 0, 2, 6, 12, 20, -45, 90, 0, 0],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task9(test_case.given),
        )
