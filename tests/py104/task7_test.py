import pytest

from src.py104.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        TestCase(given=[], expected=0),
        TestCase(given=[1, 2, 3, 4, 5], expected=1),
        TestCase(given=[3, 2, 1, 4, 5], expected=1),
        TestCase(given=[-100, -90, -10, 1, -2, 3], expected=-100),
        TestCase(given=[-100, -90, -100, 1, -2, 3], expected=-100),
        TestCase(given=[-10, -20, -30, -40, -50], expected=-50),
        TestCase(given=[9, 9, 9, 9, 9], expected=9),
        TestCase(given=[-1, 0, 1, 2, 3, 4, 5, -9, -10, 0, 100], expected=-10),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task7(test_case.given),
        )
