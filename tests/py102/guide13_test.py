import pytest

from src.py102.guide13 import guide13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide13:
    test_cases = [
        TestCase(given="INNDNIF", expected=True),
        TestCase(given="DININN", expected=True),
        TestCase(given="ININD", expected=True),
        TestCase(given="ISNISF", expected=False),
        TestCase(given="SSSS", expected=False),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sales = test_case.given

        assert_equals(
            message=f"> sales = {sales}",
            expected=test_case.expected,
            actual=guide13(sales=sales),
        )
