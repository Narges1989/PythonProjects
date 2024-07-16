import pytest

from src.py103.guide16 import guide16
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide16:
    test_cases = [
        TestCase(given="ABCDEFGH", expected="ACEG"),
        TestCase(given="I like programming", expected="Ilk rgamn"),
        TestCase(given="Sweden", expected="See"),
        TestCase(given="Panama", expected="Pnm"),
        TestCase(
            given="I speak english, spanish, and swedish",
            expected="Isekegih pns,adseih",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        sentence = test_case.given

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=test_case.expected,
            actual=guide16(sentence=sentence),
        )
