import pytest

from src.py102.guide3 import guide3
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide3:
    test_cases = [
        TestCase(given=5.0, expected=523.598),
        TestCase(given=0.0, expected=0.0),
        TestCase(given=12.4, expected=7986.45),
        TestCase(given=11.9, expected=7058.77),
        TestCase(given=15.0, expected=14137.16),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        radius = test_case.given

        assert_almost_equals(
            message=f"> radius = {radius}",
            expected=test_case.expected,
            actual=guide3(radius),
        )
