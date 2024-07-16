import pytest

from src.py102.task3 import task3
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        TestCase(given=10.0, expected=62.83185),
        TestCase(given=1.0, expected=6.283185),
        TestCase(given=5.0, expected=31.41593),
        TestCase(given=12.0, expected=75.39822),
        TestCase(given=100.0, expected=628.3185),
        TestCase(given=0.0, expected=0.0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_almost_equals(
            message=f"> radius= {test_case.given}",
            expected=test_case.expected,
            actual=task3(test_case.given),
        )
