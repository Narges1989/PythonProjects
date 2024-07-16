import pytest

from src.py103.guide8 import guide8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide8:
    test_cases = [
        TestCase(given=1, expected="monday"),
        TestCase(given=2, expected="tuesday"),
        TestCase(given=3, expected="wednesday"),
        TestCase(given=4, expected="thursday"),
        TestCase(given=5, expected="friday"),
        TestCase(given=6, expected="saturday"),
        TestCase(given=7, expected="sunday"),
        TestCase(given=0, expected="error"),
        TestCase(given=-1, expected="error"),
        TestCase(given=8, expected="error"),
        TestCase(given=100, expected="error"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        day = test_case.given

        assert_equals(
            message=f"> day = {day}",
            expected=test_case.expected,
            actual=guide8(day=day),
        )
