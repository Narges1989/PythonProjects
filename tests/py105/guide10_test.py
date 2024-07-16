import pytest

from src.py105.guide10 import guide10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide10:
    test_cases = [
        TestCase(given=[], expected={}),
        TestCase(
            given=["Mario", "Luigi", "Bowser", "Wario"],
            expected={"Mario": 1, "Luigi": 1, "Bowser": 1, "Wario": 1},
        ),
        TestCase(
            given=["Anna", "Anja", "Mary", "Anna"],
            expected={"Anna": 2, "Anja": 1, "Mary": 1},
        ),
        TestCase(
            given=["Anna", "Angela", "anna", "Mariam"],
            expected={"Anna": 1, "anna": 1, "Angela": 1, "Mariam": 1},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        names = test_case.given

        assert_equals(
            message=f"> names = {names}",
            expected=test_case.expected,
            actual=guide10(names),
        )
