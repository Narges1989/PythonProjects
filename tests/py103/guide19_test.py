import pytest

from src.py103.guide19 import guide19
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide19:
    test_cases = [
        TestCase(given="AbCd", expected="dCbA"),
        TestCase(given="123456", expected="654321"),
        TestCase(given="XyZ", expected="ZyX"),
        TestCase(given="QWERTYUIOP", expected="POIUYTREWQ"),
        TestCase(given="", expected=""),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sentence = test_case.given

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=test_case.expected,
            actual=guide19(sentence=sentence),
        )
