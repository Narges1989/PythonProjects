import pytest

from src.py105.task11 import task11
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask11:
    test_cases = [
        TestCase2(
            given1={20: "Ana", 40: "John"},
            given2=20,
            expected=True,
        ),
        TestCase2(
            given1={30: "Lise", 40: "John", 32: "Lola"},
            given2=32,
            expected=True,
        ),
        TestCase2(
            given1={20: "Ana", 40: "John", 22: "Popa"},
            given2=40,
            expected=True,
        ),
        TestCase2(
            given1={20: "Ana", 40: "John", 22: "Popa"},
            given2=57,
            expected=False,
        ),
        TestCase2(
            given1={1: "A", 2: "B", 3: "C"},
            given2=10,
            expected=False,
        ),
        TestCase2(
            given1={1: "10"},
            given2=-1,
            expected=False,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> mapa= {test_case.given1}\n> prospect= {test_case.given2}",
            expected=test_case.expected,
            actual=task11(test_case.given1, test_case.given2),
        )
