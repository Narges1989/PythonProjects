import pytest

from src.py102.guide4 import guide4
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide4:
    test_cases = [
        TestCase(given=5.0, expected=20.0),
        TestCase(given=0.0, expected=0.0),
        TestCase(given=7.1, expected=28.4),
        TestCase(given=17.90, expected=71.6),
        TestCase(given=8.9, expected=35.6),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        length = test_case.given

        assert_almost_equals(
            message=f"> length = {length}",
            expected=test_case.expected,
            actual=guide4(length),
        )
