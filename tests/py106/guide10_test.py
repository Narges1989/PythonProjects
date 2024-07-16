import pytest

from src.py106.guide10 import guide10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide10:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[None, None, None], expected=[]),
        TestCase(
            given=["apple", "ibm", None, "netflix", None],
            expected=["ApPlE", "IbM", "NeTfLiX"],
        ),
        TestCase(given=["spaces", "toyota", None, None], expected=["SpAcEs", "ToYoTa"]),
        TestCase(
            given=["apple", "ibm", "toyota", "spaces"],
            expected=["ApPlE", "IbM", "ToYoTa", "SpAcEs"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        companies = test_case.given

        assert_equals(
            message=f"> companies = {companies}",
            expected=sorted(test_case.expected),
            actual=sorted(guide10(companies=companies)),
        )
