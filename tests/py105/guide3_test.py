import pytest

from src.py105.guide3 import guide3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide3:
    test_cases = [
        TestCase2(
            given1={"Jane": 10.0, "John": 9.5, "Petter": 8.0},
            given2=["Petter", "Jose", "Richard", "Ana"],
            expected="Petter",
        ),
        TestCase2(
            given1={"Jane": 10.0, "John": 9.5, "Petter": 8.0},
            given2=["Petter", "Jane", "Richard", "Ana"],
            expected="Jane",
        ),
        TestCase2(
            given1={"Jane": 10.0, "John": 9.5, "Petter": 8.0},
            given2=["Mark", "Richard", "Ana"],
            expected="",
        ),
        TestCase2(
            given1={"Jane": 0.0},
            given2=["Jane", "Richard", "Ana"],
            expected="Jane",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given1
        students = test_case.given2

        assert_equals(
            message=f"> classroom = {classroom}\n> students = {students}",
            expected=test_case.expected,
            actual=guide3(classroom, students),
        )
