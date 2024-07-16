import pytest

from src.py105.task14 import task14
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask14:
    test_cases = [
        TestCase(given="AAAAaaaaa b", expected="a"),
        TestCase(given="AAaa BbBbbBBb XXXXX", expected="b"),
        TestCase(given="worddddWwWW", expected="w"),
        TestCase(given="We are it", expected="e"),
        TestCase(given="HeLLo Wo, OOOh No.", expected="o"),
        TestCase(given="Pa: na. ma;   ", expected="a"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task14(test_case.given),
        )
