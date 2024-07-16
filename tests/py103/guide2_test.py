import pytest

from src.py103.guide2 import guide2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide2:
    test_cases = [
        TestCase(given="December", expected=False),
        TestCase(given="May", expected=False),
        TestCase(given="July", expected=False),
        TestCase(given="November", expected=True),
        TestCase(given="november", expected=True),
        TestCase(given="NOVEMBER", expected=True),
        TestCase(given="NOvEmBeR", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        month = test_case.given

        assert_equals(
            message=f"> month = {month}",
            expected=test_case.expected,
            actual=guide2(month=month),
        )
