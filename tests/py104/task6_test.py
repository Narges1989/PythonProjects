import pytest

from src.py104.task6 import task6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask6:
    test_cases = [
        TestCase(given="", expected=""),
        TestCase(given="kotlin", expected="KoTlIn"),
        TestCase(given="I LOVE SWEDEN", expected="I LOVE SWEDEN"),
        TestCase(given="abcde", expected="AbCdE"),
        TestCase(given="abcdef abcde abcde", expected="AbCdEf aBcDe aBcDe"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task6(test_case.given),
        )
