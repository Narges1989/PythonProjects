import pytest

from src.py105.task10 import task10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask10:
    test_cases = [
        TestCase(
            given={},
            expected={},
        ),
        TestCase(
            given={20: "Ana", 40: "John"},
            expected={"Ana": 20, "John": 40},
        ),
        TestCase(
            given={30: "Lise", 40: "John", 32: "Lola"},
            expected={"Lise": 30, "John": 40, "Lola": 32},
        ),
        TestCase(
            given={20: "Ana", 40: "John", 22: "Popa"},
            expected={"Ana": 20, "John": 40, "Popa": 22},
        ),
        TestCase(
            given={1: "A", 2: "B", 3: "C"},
            expected={"A": 1, "B": 2, "C": 3},
        ),
        TestCase(
            given={1: "10"},
            expected={"10": 1},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> mapa= {test_case.given}",
            expected=test_case.expected,
            actual=task10(test_case.given),
        )
