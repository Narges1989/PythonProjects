import pytest

from src.py106.guide2 import guide2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide2:
    test_cases = [
        TestCase(given=lambda: zero_division_error(), expected=""),
        TestCase(given=lambda: ["Jane", "John", "Humberto"], expected="Humberto"),
        TestCase(given=lambda: ["Jane", "John", "Annalu", "Jade"], expected="Annalu"),
        TestCase(given=lambda: ["Esther", "Johan", "Ann", "Jade"], expected="Esther"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message="The function `script()` is given",
            expected=test_case.expected,
            actual=guide2(script=test_case.given),
        )


def zero_division_error():
    raise ZeroDivisionError("Error is thrown")
