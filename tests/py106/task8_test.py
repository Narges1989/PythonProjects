import pytest

from src.py106.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        TestCase(
            given=[],
            expected=[],
        ),
        TestCase(
            given=["hej", "kr", "I", ""],
            expected=[],
        ),
        TestCase(
            given=[None, None, None],
            expected=[],
        ),
        TestCase(
            given=["ok", "SEK", "Hello", "Gothenburg", None],
            expected=["Hello", "Gothenburg"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task8(test_case.given),
        )
