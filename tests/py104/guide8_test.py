import pytest

from src.py104.guide8 import guide8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide8:
    test_cases = [
        TestCase(given=["Panama", "Costa Rica"], expected=[]),
        TestCase(
            given=["Sweden", "Panama", "Canada", "Denmark", "Spain"],
            expected=["Sweden", "Denmark"],
        ),
        TestCase(
            given=["Ireland", "Netherlands", "Sweden", "Hungary", "Norway"],
            expected=["Sweden", "Norway"],
        ),
        TestCase(
            given=[
                "Iceland",
                "Austria",
                "Greenland",
                "Germany",
                "Portugal",
                "Poland",
                "Åland",
                "Faroe Islands",
            ],
            expected=["Iceland", "Greenland", "Åland", "Faroe Islands"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide8(items)),
        )
