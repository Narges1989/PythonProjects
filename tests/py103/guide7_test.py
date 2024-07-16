import pytest

from src.py103.guide7 import guide7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide7:
    test_cases = [
        TestCase(given=9, expected="fall"),
        TestCase(given=10, expected="fall"),
        TestCase(given=11, expected="fall"),
        TestCase(given=12, expected="winter"),
        TestCase(given=1, expected="winter"),
        TestCase(given=2, expected="winter"),
        TestCase(given=3, expected="spring"),
        TestCase(given=4, expected="spring"),
        TestCase(given=5, expected="spring"),
        TestCase(given=6, expected="summer"),
        TestCase(given=7, expected="summer"),
        TestCase(given=8, expected="summer"),
        TestCase(given=13, expected="error"),
        TestCase(given=-1, expected="error"),
        TestCase(given=0, expected="error"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        month = test_case.given

        assert_equals(
            message=f"> month = {month}",
            expected=test_case.expected,
            actual=guide7(month=month),
        )
