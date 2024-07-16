import pytest

from linero_tech_errors import LowAttendanceError, MissingGradesError
from src.py106.guide3 import guide3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide3:
    test_cases = [
        TestCase(given=lambda: missing_grade_error(), expected=-1.0),
        TestCase(given=lambda: low_attendance_error(), expected=-2.0),
        TestCase(given=lambda: [4.55, 2.0, 2.5], expected=4.55),
        TestCase(given=lambda: [4.3, 5.0, 4.5], expected=5.0),
        TestCase(given=lambda: [1.6, 1.5, 2.0], expected=2.0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message="The function `script()` is given",
            expected=test_case.expected,
            actual=guide3(script=test_case.given),
        )


def missing_grade_error():
    raise MissingGradesError()


def low_attendance_error():
    raise LowAttendanceError()
