import pytest

from src.py103.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask5:
    test_cases = [
        TestCase(given="", expected=0),
        TestCase(given="Hello", expected=5),
        TestCase(given="Sweden in beautiful", expected=19),
        TestCase(given="I like Kotlin", expected=13),
        TestCase(given="You will learn Kotlin", expected=21),
        TestCase(given="Kotlin is for Android and much more", expected=35),
        TestCase(given="You are learning how to program", expected=31),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task5(test_case.given),
        )
