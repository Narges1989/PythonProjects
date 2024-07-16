import pytest

from src.py104.guide2 import guide2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide2:
    test_cases = [
        TestCase(given=[], expected=-1),
        TestCase(given=[10], expected=-1),
        TestCase(given=[10, 20], expected=-1),
        TestCase(given=[10, 20, 40, 50], expected=-1),
        TestCase(given=[10, 20, 60, 70, 80], expected=-1),
        TestCase(given=[80, 80, 80], expected=80),
        TestCase(given=[100, 90, 80], expected=100),
        TestCase(given=[90, 95, 70], expected=95),
        TestCase(given=[40, 45, 60], expected=60),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> item = {items}",
            expected=test_case.expected,
            actual=guide2(items),
        )
