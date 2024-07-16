import pytest

from src.py105.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        TestCase(given={}, expected=0),
        TestCase(given={1: 10}, expected=1),
        TestCase(given={1: 10, 2: 20, 3: 30}, expected=6),
        TestCase(given={1: 100, 2: 200, 3: 200, 10: 122, 7: 87}, expected=23),
        TestCase(given={100: 2, 50: 25, 15: 200, 10: 122, 25: 87}, expected=200),
        TestCase(given={-1: 100, 1: 200, -2: 200, 2: 122, 3: 87}, expected=3),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> mapa= {test_case.given}",
            expected=test_case.expected,
            actual=task2(test_case.given),
        )
