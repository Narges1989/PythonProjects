import pytest

from src.py104.guide6 import guide6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide6:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[1, 2, 3, 4], expected=[]),
        TestCase(given=[5, 50, 55, 25, 10, 5], expected=[50, 55, 25]),
        TestCase(given=[5, 6, 7, 8, 10, 15, 25, 5, 25], expected=[15, 25, 25]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide6(items)),
        )
