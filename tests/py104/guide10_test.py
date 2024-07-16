import pytest

from src.py104.guide10 import guide10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide10:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=["a", "B"], expected=["A", "b"]),
        TestCase(given=["A", "B"], expected=["A", "b"]),
        TestCase(given=["a", "b"], expected=["A", "b"]),
        TestCase(
            given=["a", "B", "hola", "foo", "bar", "qix"],
            expected=["A", "b", "HOLA", "foo", "BAR", "qix"],
        ),
        TestCase(
            given=["Kotlin", "Python", "Linero Tech", "JetBrains"],
            expected=["KOTLIN", "python", "LINERO TECH", "jetbrains"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide10(items)),
        )
