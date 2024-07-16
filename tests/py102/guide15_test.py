import pytest

from src.py102.guide15 import guide15
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide15:
    test_cases = [
        TestCase(given="IDDDIF", expected=0),
        TestCase(given="DIDSFF", expected=1),
        TestCase(given="ISIND", expected=2),
        TestCase(given="ISNNISFDDS", expected=5),
        TestCase(given="SSSSNNN", expected=7),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide15(sales=sales),
        )
