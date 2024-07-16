import pytest

from src.py102.guide10 import guide10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide10:
    test_cases = [
        TestCase(given="DDNNNNIS", expected="S"),
        TestCase(given="SINISND", expected="D"),
        TestCase(given="IDNISF", expected="F"),
        TestCase(given="DDSIN", expected="N"),
        TestCase(given="NDNI", expected="I"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide10(sales=sales),
        )
