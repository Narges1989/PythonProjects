import pytest

from src.py103.guide17 import guide17
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide17:
    test_cases = [
        TestCase(given="ABCDEFGH", expected="AbCdEfGh"),
        TestCase(given="abcdefgh", expected="AbCdEfGh"),
        TestCase(given="I like programming", expected="I LiKe pRoGrAmMiNg"),
        TestCase(given="Sweden", expected="SwEdEn"),
        TestCase(given="sWeDeN", expected="SwEdEn"),
        TestCase(given="Panama", expected="PaNaMa"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sentence = test_case.given

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=test_case.expected,
            actual=guide17(sentence=sentence),
        )
