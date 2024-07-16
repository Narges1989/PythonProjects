import pytest

from src.py105.guide4 import guide4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide4:
    test_cases = [
        TestCase2(
            given1={"cheese": 10.0, "eggs": 5.0, "milk": 30.0}, given2=[], expected=0.0
        ),
        TestCase2(
            given1={"cheese": 10.0, "eggs": 5.0, "milk": 30.0},
            given2=["ham", "pizza", "bread"],
            expected=0.0,
        ),
        TestCase2(
            given1={"cheese": 10.0, "eggs": 5.0, "milk": 30.7},
            given2=["ham", "pizza", "bread", "milk", "soda"],
            expected=30.7,
        ),
        TestCase2(
            given1={"cheese": 10.1, "eggs": 5.0, "milk": 30.7},
            given2=["ham", "pizza", "cheese", "bread", "milk"],
            expected=40.8,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        supermarket = test_case.given1
        ingredients = test_case.given2

        assert_equals(
            message=f"> supermarket = {supermarket}\n> ingredients = {ingredients}",
            expected=test_case.expected,
            actual=guide4(supermarket, ingredients),
        )
