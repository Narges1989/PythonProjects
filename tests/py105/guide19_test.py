import pytest

from src.py105.guide19 import guide19
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide19:
    test_cases = [
        TestCase(
            given={
                "pizza": {"price": 1.5, "brand": "Bonlac"},
            },
            expected="pizza",
        ),
        TestCase(
            given={
                "apple": {"price": 1.5, "brand": "Bonlac"},
                "cheese": {"price": 5.2, "brand": "Young"},
                "yogurt": {"price": 3.0, "brand": "Bonlac"},
            },
            expected="apple",
        ),
        TestCase(
            given={
                "milk": {"price": 1.5, "brand": "Bonlac"},
                "beans": {"price": 1.0, "brand": "Young"},
                "yogurt": {"price": 3.0, "brand": "Bonlac"},
            },
            expected="beans",
        ),
        TestCase(
            given={
                "milk": {"price": 10.5, "brand": "Bonlac"},
                "cheese": {"price": 5.2, "brand": "Young"},
                "yogurt": {"price": 3.0, "brand": "Bonlac"},
            },
            expected="yogurt",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        supermarket = test_case.given

        assert_equals(
            message=f"> supermarket = {supermarket}",
            expected=test_case.expected,
            actual=guide19(supermarket),
        )
