import pytest

from src.py102.guide9 import guide9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide9:
    test_cases = [
        TestCase(given="NDNSNNID", expected="S"),
        TestCase(given="SSNDSNI", expected="D"),
        TestCase(given="DDNFSN", expected="F"),
        TestCase(given="SDSNS", expected="N"),
        TestCase(given="SDNI", expected="I"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide9(sales=sales),
        )
