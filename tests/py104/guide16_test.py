import pytest

from src.py104.guide16 import guide16
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide16:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=["John", "Jane", "Ehenola", "Joseph"], expected=[]),
        TestCase(given=["Susan", "Honda", "Sandra", "Chi"], expected=["Honda"]),
        TestCase(
            given=["Pat", "Moi", "Helen", "Joshua", "Hundai"],
            expected=["Helen", "Hundai"],
        ),
        TestCase(
            given=["Elena", "Helen", "Humberto", "John", "Henry"],
            expected=["Helen", "Humberto", "Henry"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide16(items)),
        )
