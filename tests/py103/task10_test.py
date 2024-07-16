import pytest

from src.py103.task10 import task10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask10:
    test_cases = [
        TestCase(given="asc", expected=False),
        TestCase(given="a4fA", expected=False),
        TestCase(given="ah8&F", expected=False),
        TestCase(given="Ba#2HS#@B1@Hf#1Iy#1", expected=False),
        TestCase(given="B#2G@A#", expected=False),
        TestCase(given="b#2h@e#", expected=False),
        TestCase(given="Ga@GJDa", expected=False),
        TestCase(given="A1a5b5d", expected=False),
        TestCase(given="A1a@#gus", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> password= {test_case.given}",
            expected=test_case.expected,
            actual=task10(test_case.given),
        )
