import pytest

from src.py104.guide15 import guide15
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide15:
    test_cases = [
        TestCase(given=["John", "Jane", "Jade"], expected=True),
        TestCase(given=["John", "Jane", "Roberto", "Mary", "Persona"], expected=True),
        TestCase(
            given=["Ron", "Petter", "Lina", "Luna", "Merche", "Mona", "Menlo"],
            expected=False,
        ),
        TestCase(
            given=[
                "Ricauter",
                "Maria",
                "Johanna",
                "Fletcher",
                "Lucas",
                "Patrik",
                "Airan",
                "Fercho",
                "Del",
            ],
            expected=False,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=test_case.expected,
            actual=guide15(items),
        )
