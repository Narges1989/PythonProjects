import pytest

from src.py105.task15 import task15
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask15:
    test_cases = [
        TestCase(
            given="This is the Very small Text",
            expected={"i": 1, "s": 1, "t": 3, "v": 1},
        ),
        TestCase(
            given="I am it",
            expected={"a": 1, "i": 2},
        ),
        TestCase(
            given="AAaa BB",
            expected={"a": 1, "b": 1},
        ),
        TestCase(
            given="word WwW",
            expected={"w": 2},
        ),
        TestCase(
            given="This is not a very very very small text",
            expected={"a": 1, "i": 1, "n": 1, "s": 1, "t": 2, "v": 3},
        ),
        TestCase(
            given="No word is repeated in this sentence",
            expected={"i": 2, "n": 1, "r": 1, "s": 1, "t": 1, "w": 1},
        ),
        TestCase(
            given="this This THIS is still the very very same",
            expected={"i": 1, "s": 2, "t": 4, "v": 2},
        ),
        TestCase(
            given="this, This; THIS, is still the very very same",
            expected={"i": 1, "s": 2, "t": 4, "v": 2},
        ),
        TestCase(
            given="word",
            expected={"w": 1},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task15(test_case.given),
        )
