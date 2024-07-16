import pytest

from src.py105.task6 import task6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask6:
    test_cases = [
        TestCase2(
            given1={},
            given2="anything",
            expected={},
        ),
        TestCase2(
            given1={20: "Ana", 40: "John", 22: "Ana"},
            given2="Ana",
            expected={20: "Ana", 22: "Ana"},
        ),
        TestCase2(
            given1={20: "Ana", 40: "John", 22: "Ana"},
            given2="John",
            expected={40: "John"},
        ),
        TestCase2(
            given1={20: "Ana", 40: "John", 22: "Ana"},
            given2="Mark",
            expected={},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> mapa= {test_case.given1}\n> parameter= {test_case.given2}",
            expected=test_case.expected,
            actual=task6(test_case.given1, test_case.given2),
        )
