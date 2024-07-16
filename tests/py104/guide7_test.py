import pytest

from src.py104.guide7 import guide7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide7:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[1, 3, 5, 7], expected=[0, 3, 10, 21]),
        TestCase(given=[2, 4, 6, 8, 0], expected=[0, 4, 12, 24, 0]),
        TestCase(given=[10, 11, 12, 13, 14], expected=[0, 11, 24, 39, 56]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide7(items)),
        )
