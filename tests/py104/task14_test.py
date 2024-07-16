import pytest

from src.py104.task14 import task14
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask14:
    test_cases = [
        TestCase(given=[10000, 2000, 800, 768, 765, 90, 10], expected="Sunday"),
        TestCase(given=[100, 2000, 800, 768, 765, 10, 100], expected="Saturday"),
        TestCase(given=[100, 2000, 80000, 768, 10, 90, 100], expected="Friday"),
        TestCase(given=[100, 2000, 800, 10, 101, 90, 300], expected="Thursday"),
        TestCase(given=[100, 2000, 10, 768, 76235, 90, 300], expected="Wednesday"),
        TestCase(given=[100, 10, 800, 768, 765, 9000, 300], expected="Tuesday"),
        TestCase(given=[10, 2000, 800, 768, 765, 9000, 10000], expected="Monday"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sells= {test_case.given}",
            expected=test_case.expected,
            actual=task14(test_case.given),
        )
