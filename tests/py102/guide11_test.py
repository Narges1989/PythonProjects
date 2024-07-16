import pytest

from src.py102.guide11 import guide11
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide11:
    test_cases = [
        TestCase(given="DDNNNNIS", expected="DDNNN"),
        TestCase(given="SINISND", expected="SINIS"),
        TestCase(given="IDNISF", expected="IDNIS"),
        TestCase(given="DDSIN", expected="DDSIN"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide11(sales=sales),
        )
