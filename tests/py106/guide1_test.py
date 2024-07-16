import pytest

from src.py106.guide1 import guide1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide1:
    test_cases = [
        TestCase(given=lambda: file_not_found_error(), expected=[]),
        TestCase(given=lambda: [1, 2, 3, 4], expected=[0, 2, 6, 12]),
        TestCase(given=lambda: [55, 33, 44, 77], expected=[0, 33, 88, 231]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message="The function `script()` is given",
            expected=test_case.expected,
            actual=guide1(script=test_case.given),
        )


def file_not_found_error():
    raise FileNotFoundError("Error is thrown")
