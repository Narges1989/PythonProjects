import pytest

from src.py104.guide22 import guide22
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide22:
    test_cases = [
        TestCase(given=1, expected={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}),
        TestCase(given=5, expected={5, 10, 15, 20, 25, 30, 35, 40, 45, 50}),
        TestCase(given=10, expected={10, 20, 30, 40, 50, 60, 70, 80, 90, 100}),
        TestCase(given=2, expected={2, 4, 6, 8, 10, 12, 14, 16, 18, 20}),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given

        assert_equals(
            message=f"> a = {a}",
            expected=test_case.expected,
            actual=guide22(a),
        )
