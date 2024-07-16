import pytest

from src.py102.guide12 import guide12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide12:
    test_cases = [
        TestCase(given="DDNNNNIS", expected=8),
        TestCase(given="SINISND", expected=7),
        TestCase(given="IDNISF", expected=6),
        TestCase(given="DDSIN", expected=5),
        TestCase(given="NDNI", expected=4),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide12(sales=sales),
        )
