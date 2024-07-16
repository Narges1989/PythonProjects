import pytest

from src.py104.guide3 import guide3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide3:
    test_cases = [
        TestCase(given=[], expected=-1),
        TestCase(
            given=["Portugal", "Norway", "Italy", "Panama", "France", "Austria"],
            expected=40,
        ),
        TestCase(
            given=["Colombia", "Norway", "Italy", "Panama", "France"], expected=32
        ),
        TestCase(given=["Sweden", "Norway", "Italy", "Panama"], expected=18),
        TestCase(given=["Italy", "Norway", "Germany"], expected=10),
        TestCase(given=["Norway", "Norway"], expected=6),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=test_case.expected,
            actual=guide3(items),
        )
