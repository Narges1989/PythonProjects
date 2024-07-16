import pytest

from linero_tech_errors import InvalidAgeError, MissingAgeError
from src.py106.guide4 import guide4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide4:
    test_cases = [
        TestCase(given=lambda: invalid_age_error(), expected=[0, 0, 0]),
        TestCase(given=lambda: missing_age_error(), expected=[1, 1, 1]),
        TestCase(given=lambda: [10, 45, 17, 18, 20, 21], expected=[45, 18, 20, 21]),
        TestCase(given=lambda: [10, 15, 13, 17, 11], expected=[]),
        TestCase(given=lambda: [18, 20, 19, 30], expected=[18, 20, 19, 30]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message="The function `script()` is given",
            expected=sorted(test_case.expected),
            actual=sorted(guide4(script=test_case.given)),
        )


def invalid_age_error():
    raise InvalidAgeError()


def missing_age_error():
    raise MissingAgeError()
