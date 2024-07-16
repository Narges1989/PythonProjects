import pytest

from src.py105.guide18 import guide18
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide18:
    test_cases = [
        TestCase(given=[], expected=0.0),
        TestCase(given=[{"gpa": 5.0}], expected=5.0),
        TestCase(given=[{"gpa": 10.0}, {"gpa": 9.0}, {"gpa": 7.5}], expected=8.83),
        TestCase(given=[{"gpa": 5.0}, {"gpa": 5.0}, {"gpa": 5.0}], expected=5.0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given

        assert_almost_equals(
            message=f"> classroom = {classroom}",
            expected=test_case.expected,
            actual=guide18(classroom),
        )
