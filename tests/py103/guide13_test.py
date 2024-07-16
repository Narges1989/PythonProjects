import pytest

from src.py103.guide13 import guide13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide13:
    test_cases = [
        TestCase(given=0, expected=False),
        TestCase(given=2, expected=False),
        TestCase(given=20, expected=False),
        TestCase(given=-90, expected=False),
        TestCase(given=-120, expected=False),
        TestCase(given=-13, expected=True),
        TestCase(given=-25, expected=True),
        TestCase(given=81, expected=True),
        TestCase(given=33, expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        number = test_case.given

        assert_equals(
            message=f"> number = {number}",
            expected=test_case.expected,
            actual=guide13(number=number),
        )
