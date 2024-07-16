import pytest

from src.py104.task13 import task13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask13:
    test_cases = [
        TestCase(given=[10000, 2000, 800, 768, 765, 90, 10], expected="Monday"),
        TestCase(given=[100, 2000, 800, 768, 765, 10, 100], expected="Tuesday"),
        TestCase(given=[100, 2000, 80000, 768, 10, 90, 100], expected="Wednesday"),
        TestCase(given=[100, 2000, 800, 76238, 10, 90, 300], expected="Thursday"),
        TestCase(given=[100, 2000, 10, 768, 76235, 90, 300], expected="Friday"),
        TestCase(given=[100, 10, 800, 768, 765, 9000, 300], expected="Saturday"),
        TestCase(given=[10, 2000, 800, 768, 765, 9000, 10000], expected="Sunday"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sells= {test_case.given}",
            expected=test_case.expected,
            actual=task13(test_case.given),
        )
