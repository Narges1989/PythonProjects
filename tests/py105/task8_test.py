import pytest

from src.py105.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        TestCase(
            given={
                "Ana": [4.0, 4.5, 5.0],
                "John": [5.0, 5.0, 3.0],
                "Lise": [5.0, 5.0, 5.0],
            },
            expected="Lise",
        ),
        TestCase(
            given={
                "Ana": [3.9, 2.5, 2.5],
                "John": [4.3, 4.2, 4.7],
                "Lise": [4.2, 4.3, 4.4],
            },
            expected="John",
        ),
        TestCase(
            given={"Ana": [4.0, 4.5, 5.0]},
            expected="Ana",
        ),
        TestCase(
            given={"Ana": [0.0, 0.5, 0.0]},
            expected="Ana",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> grades= {test_case.given}",
            expected=test_case.expected,
            actual=task8(test_case.given),
        )
