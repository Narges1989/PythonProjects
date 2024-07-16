import pytest

from src.py104.guide9 import guide9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide9:
    test_cases = [
        TestCase(given=[1, 5, 77, 71, 9], expected=[]),
        TestCase(given=[1, 5, 10, 60, 77, 71, 80, 9], expected=[10, 60, 80]),
        TestCase(given=[10, 20, 30, 40, 50], expected=[10, 20, 30, 40, 50]),
        TestCase(given=[2, 3, 4, 5, 6, 10, 15, 20], expected=[10, 20]),
        TestCase(
            given=[120, 130, 140, 50, 60, 10, 15, 20],
            expected=[120, 130, 140, 50, 60, 10, 20],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide9(items)),
        )
