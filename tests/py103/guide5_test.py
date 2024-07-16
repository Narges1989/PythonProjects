import pytest

from src.py103.guide5 import guide5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide5:
    test_cases = [
        TestCase(given="Oslo", expected=False),
        TestCase(given="Panama", expected=False),
        TestCase(given="Madrid", expected=False),
        TestCase(given="Berlin", expected=False),
        TestCase(given="stockholm", expected=True),
        TestCase(given="Stockholm", expected=True),
        TestCase(given="StockHOLM", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        capital = test_case.given

        assert_equals(
            message=f"> capital = {capital}",
            expected=test_case.expected,
            actual=guide5(capital=capital),
        )
