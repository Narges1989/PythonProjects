import pytest

from src.py105.guide15 import guide15
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide15:
    test_cases = [
        TestCase(given={}, expected={}),
        TestCase(
            given={"Rita": 1, "Jay": 5}, expected={"Rita": "Winter", "Jay": "Spring"}
        ),
        TestCase(
            given={"Mario": 3, "Wario": 11, "Luigi": 2, "Nora": 7},
            expected={
                "Mario": "Spring",
                "Wario": "Fall",
                "Luigi": "Winter",
                "Nora": "Summer",
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        birthdays = test_case.given

        assert_equals(
            message=f"> birthdays = {birthdays}",
            expected=test_case.expected,
            actual=guide15(birthdays),
        )
