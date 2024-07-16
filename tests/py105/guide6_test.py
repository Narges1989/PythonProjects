import pytest

from src.py105.guide6 import guide6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase3


class TestGuide6:
    test_cases = [
        TestCase3(given1={}, given2="a", given3=1, expected=0),
        TestCase3(
            given1={
                "Ana": 1,
                "Anja": 1,
                "Mary": 5,
                "attiq": 1,
                "Amber": 5,
                "anders": 7,
            },
            given2="n",
            given3=1,
            expected=0,
        ),
        TestCase3(
            given1={"Ana": 1, "April": 1, "Sofia": 5, "Juan": 1, "Mauri": 5, "Kath": 7},
            given2="a",
            given3=11,
            expected=0,
        ),
        TestCase3(
            given1={
                "Ana": 1,
                "Anja": 1,
                "Mary": 5,
                "attiq": 1,
                "Amber": 5,
                "anders": 7,
            },
            given2="a",
            given3=1,
            expected=3,
        ),
        TestCase3(
            given1={
                "Ana": 1,
                "Anja": 1,
                "Mary": 5,
                "attiq": 1,
                "Amber": 5,
                "anders": 7,
            },
            given2="A",
            given3=1,
            expected=3,
        ),
        TestCase3(
            given1={
                "Ana": 1,
                "Anja": 1,
                "Mary": 1,
                "attiq": 1,
                "Amber": 5,
                "anders": 7,
            },
            given2="A",
            given3=1,
            expected=3,
        ),
        TestCase3(
            given1={
                "Anna": 1,
                "Ania": 1,
                "Mary": 5,
                "Andrea": 1,
                "Amber": 5,
                "anders": 7,
            },
            given2="a",
            given3=5,
            expected=1,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        birthdays = test_case.given1
        letter = test_case.given2
        month = test_case.given3

        assert_equals(
            message=f"> birthdays = {birthdays}\n> letter = {letter}\n> month = {month}",
            expected=test_case.expected,
            actual=guide6(birthdays, letter, month),
        )
