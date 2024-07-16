import pytest

from src.py106.task4 import task4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask4:
    test_cases = [
        TestCase(
            given="",
            expected={},
        ),
        TestCase(
            given=None,
            expected={},
        ),
        TestCase(
            given="Hello",
            expected={"a": 0, "e": 1, "i": 0, "o": 1, "u": 0},
        ),
        TestCase(
            given="HELLO",
            expected={"a": 0, "e": 1, "i": 0, "o": 1, "u": 0},
        ),
        TestCase(
            given="I live in Sweden",
            expected={"a": 0, "e": 3, "i": 3, "o": 0, "u": 0},
        ),
        TestCase(
            given="I LIVE IN SWEDEN",
            expected={"a": 0, "e": 3, "i": 3, "o": 0, "u": 0},
        ),
        TestCase(
            given="I LiVE iN SwEDeN",
            expected={"a": 0, "e": 3, "i": 3, "o": 0, "u": 0},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task4(test_case.given),
        )
