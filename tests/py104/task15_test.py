import pytest

from src.py104.task15 import task15
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask15:
    test_cases = [
        TestCase(given=[10000, 2000, 800, 768, 765, 90, 10], expected=14433),
        TestCase(given=[100, 2000, 800, 768, 765, 10, 100], expected=4543),
        TestCase(given=[100, 2000, 80000, 768, 10, 90, 100], expected=83068),
        TestCase(given=[100, 2000, 800, 10, 101, 90, 300], expected=3401),
        TestCase(given=[100, 2000, 800, 76238, 10, 90, 300], expected=79538),
        TestCase(given=[100, 2000, 10, 768, 76235, 90, 300], expected=79503),
        TestCase(given=[100, 10, 800, 768, 765, 9000, 300], expected=11743),
        TestCase(given=[10, 2000, 800, 768, 765, 9000, 10000], expected=23343),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sells= {test_case.given}",
            expected=test_case.expected,
            actual=task15(test_case.given),
        )
