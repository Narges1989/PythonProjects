import pytest

from src.py104.task10 import task10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask10:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[1, 2, 3, 4, 5], expected=[3, 4, 9, 8, 15]),
        TestCase(given=[4], expected=[8]),
        TestCase(given=[1, 1, 1], expected=[3, 3, 3]),
        TestCase(given=[2, 2, 2], expected=[4, 4, 4]),
        TestCase(
            given=[11, 0, 1, 2, 3, 41, 5, 90, 50, 0, 100],
            expected=[33, 0, 3, 4, 9, 123, 15, 180, 100, 0, 200],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task10(test_case.given),
        )
