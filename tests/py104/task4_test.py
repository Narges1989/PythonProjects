import pytest

from src.py104.task4 import task4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask4:
    test_cases = [
        TestCase2(given1=[], given2=5, expected=[]),
        TestCase2(given1=[1, 2, 4, 5, 6], given2=2, expected=[2, 4, 6]),
        TestCase2(given1=[12, 16, 21, 18, 9], given2=3, expected=[12, 21, 18, 9]),
        TestCase2(given1=[25, 10, 5, 3, 40], given2=5, expected=[25, 10, 5, 40]),
        TestCase2(given1=[25, 25, 25, 25, 25], given2=5, expected=[25]),
        TestCase2(given1=[250, 50, 250, 50, 30], given2=10, expected=[250, 50, 30]),
        TestCase2(given1=[1, 2, 3, 4, 5, 6, 7, 8], given2=5, expected=[5]),
        TestCase2(
            given1=[1, 2, 3, 4, 5, 1, 2, 3, 4, 6, 7, 8, 6, 7, 9],
            given2=2,
            expected=[2, 4, 6, 8],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given1
        factor = test_case.given2

        assert_equals(
            message=f"> items= {items}\n> factor= {factor}",
            expected=sorted(test_case.expected),
            actual=sorted(task4(items, factor)),
        )
