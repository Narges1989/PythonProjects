import pytest

from src.py103.guide12 import guide12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide12:
    test_cases = [
        TestCase(given=0, expected=True),
        TestCase(given=2, expected=True),
        TestCase(given=20, expected=True),
        TestCase(given=-90, expected=True),
        TestCase(given=-120, expected=True),
        TestCase(given=-13, expected=False),
        TestCase(given=-25, expected=False),
        TestCase(given=81, expected=False),
        TestCase(given=33, expected=False),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        number = test_case.given

        assert_equals(
            message=f"> number = {number}",
            expected=test_case.expected,
            actual=guide12(number=number),
        )
