import pytest

from src.py103.task6 import task6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask6:
    test_cases = [
        TestCase(given=191, expected=191),
        TestCase(given=284, expected=482),
        TestCase(given=11, expected=11),
        TestCase(given=5, expected=5),
        TestCase(given=12, expected=21),
        TestCase(given=1234, expected=4321),
        TestCase(given=23, expected=32),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> number= {test_case.given}",
            expected=test_case.expected,
            actual=task6(test_case.given),
        )
