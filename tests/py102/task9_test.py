import pytest

from src.py102.task9 import task9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask9:
    test_cases = [
        # given1 is sentence, given2 is character
        TestCase2(given1="", given2="H", expected=False),
        TestCase2(given1="Vasa 1", given2="1", expected=True),
        TestCase2(given1="Stockholm", given2="H", expected=True),
        TestCase2(given1="12234567", given2="2", expected=True),
        TestCase2(given1="Gothenburg is in Sweden", given2="E", expected=True),
        TestCase2(given1="Kotlin is for Android", given2="A", expected=True),
        TestCase2(given1="I AM LEARNING KOTLIN", given2="t", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sentence = test_case.given1
        character = test_case.given2

        assert_equals(
            message=f"> sentence= {sentence}\n> character= {character}",
            expected=test_case.expected,
            actual=task9(sentence, character),
        )
