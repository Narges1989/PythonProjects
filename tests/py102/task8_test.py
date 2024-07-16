import pytest

from src.py102.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask8:
    test_cases = [
        # given1 is sentence, given2 is character
        TestCase2(given1="", given2="H", expected=0),
        TestCase2(given1=" ", given2="A", expected=0),
        TestCase2(given1="Sweden Gothenburg", given2="e", expected=3),
        TestCase2(given1="HHHH", given2="h", expected=0),
        TestCase2(given1="12234567", given2="2", expected=2),
        TestCase2(given1="HellO World", given2="o", expected=1),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sentence = test_case.given1
        character = test_case.given2

        assert_equals(
            message=f"> sentence= {sentence}\n> character= {character}",
            expected=test_case.expected,
            actual=task8(sentence, character),
        )
