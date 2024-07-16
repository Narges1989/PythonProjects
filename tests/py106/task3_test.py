import pytest

from src.py106.task3 import task3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        TestCase(given=None, expected="*"),
        TestCase(given="", expected="*"),
        TestCase(given="Hello", expected="H*ll*"),
        TestCase(given="HELLO", expected="H*LL*"),
        TestCase(given="I live in Sweden", expected="* l*v* *n Sw*d*n"),
        TestCase(given="I LIVE IN SWEDEN", expected="* L*V* *N SW*D*N"),
        TestCase(given="I LiVE iN SwEDeN", expected="* L*V* *N Sw*D*N"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task3(test_case.given),
        )
