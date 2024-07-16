import pytest

from src.py104.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        TestCase(given=[], expected=0),
        TestCase(given=[1, 2], expected=1),
        TestCase(given=[5, 7, 9], expected=14),
        TestCase(given=[1, 2, 3, 4], expected=4),
        TestCase(given=[1, 1, -2, 3, 4], expected=3),
        TestCase(given=[0, 1, 2, 3, 4, 5], expected=6),
        TestCase(given=[0, 1, -2, 3, -4, 5, -6], expected=-12),
        TestCase(
            given=[
                8,
                9,
                0,
                6,
                3,
                6,
                8,
                4,
                6,
                456,
                3,
                5,
                3,
                7,
                4,
                5566,
                234,
                1,
                234,
                35646,
                234,
            ],
            expected=737,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task2(test_case.given),
        )
