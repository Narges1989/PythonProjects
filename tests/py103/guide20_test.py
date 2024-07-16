import pytest

from src.py103.guide20 import guide20
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide20:
    test_cases = [
        TestCase2(given1="ABCDA", given2="a", expected=0),
        TestCase2(given1="ABCDA", given2="b", expected=1),
        TestCase2(given1="AbCdA", given2="b", expected=1),
        TestCase2(given1="ABCdA", given2="D", expected=3),
        TestCase2(given1="xyzf", given2="f", expected=3),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sentence = test_case.given1
        character = test_case.given2

        assert_equals(
            message=f"> sentence = {sentence}\n> character = {character}",
            expected=test_case.expected,
            actual=guide20(sentence=sentence, character=character),
        )
