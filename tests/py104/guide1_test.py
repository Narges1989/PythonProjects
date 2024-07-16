import pytest

from src.py104.guide1 import guide1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide1:
    test_cases = [
        TestCase(given=[], expected=-1),
        TestCase(
            given=[
                1,
            ],
            expected=-1,
        ),
        TestCase(given=[1, 2], expected=-1),
        TestCase(given=[1, 2, 3], expected=-1),
        TestCase(given=[1, 2, 3, 4], expected=-1),
        TestCase(given=[10, 2, 30, 4, 50, 6], expected=90_000),
        TestCase(given=[1, 21, 1, 41, 1, 61, 3], expected=3),
        TestCase(given=[2, 21, 2, 41, 2, 4, 5, 7], expected=56),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=test_case.expected,
            actual=guide1(items),
        )
