import pytest

from src.py104.guide14 import guide14
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide14:
    test_cases = [
        TestCase(given=[1, 5, 7, 9, 10], expected=7),
        TestCase(given=[1, 5, 7, 9, 10, 90, 100], expected=9),
        TestCase(given=[10, 50, 70], expected=50),
        TestCase(given=[300, 500, 777, 1000, 665], expected=777),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=test_case.expected,
            actual=guide14(items),
        )
