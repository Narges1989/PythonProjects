import pytest

from src.py102.guide14 import guide14
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide14:
    test_cases = [
        TestCase(given="DDNNNNIF", expected=0),
        TestCase(given="SININND", expected=1),
        TestCase(given="ISNISF", expected=2),
        TestCase(given="DSSSN", expected=3),
        TestCase(given="SSSS", expected=4),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide14(sales=sales),
        )
