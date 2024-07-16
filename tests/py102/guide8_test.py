import pytest

from src.py102.guide8 import guide8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide8:
    test_cases = [
        TestCase(given="SDNFNNII", expected="S"),
        TestCase(given="DSNFSNII", expected="D"),
        TestCase(given="FSNSSNII", expected="F"),
        TestCase(given="NDSFSSII", expected="N"),
        TestCase(given="IDNFSNSS", expected="I"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide8(sales=sales),
        )
