import pytest

from src.py105.guide9 import guide9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide9:
    test_cases = [
        TestCase(
            given="",
            expected={},
        ),
        TestCase(
            given="ion",
            expected={"i": 1, "o": 1, "n": 1},
        ),
        TestCase(
            given="APplle",
            expected={"A": 1, "P": 1, "p": 1, "l": 2, "e": 1},
        ),
        TestCase(
            given="NeOn",
            expected={"N": 1, "e": 1, "O": 1, "n": 1},
        ),
        TestCase(
            given="mississippi",
            expected={"m": 1, "i": 4, "s": 4, "p": 2},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        word = test_case.given

        assert_equals(
            message=f"> word = {word}",
            expected=test_case.expected,
            actual=guide9(word),
        )
