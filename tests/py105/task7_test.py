import pytest

from src.py105.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        TestCase(
            given=[],
            expected={},
        ),
        TestCase(
            given=["I", "love", "Kotlin"],
            expected={0: "I", 1: "love", 2: "Kotlin"},
        ),
        TestCase(
            given=["Gbg", "is", "amazing"],
            expected={0: "Gbg", 1: "is", 2: "amazing"},
        ),
        TestCase(
            given=["Sweden", "is", "in", "Europe"],
            expected={0: "Sweden", 1: "is", 2: "in", 3: "Europe"},
        ),
        TestCase(
            given=["1", "2", "3", "4"],
            expected={0: "1", 1: "2", 2: "3", 3: "4"},
        ),
        TestCase(
            given=["1"],
            expected={0: "1"},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> words= {test_case.given}",
            expected=test_case.expected,
            actual=task7(test_case.given),
        )
