import pytest

from src.py106.guide8 import guide8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide8:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(
            given1=1,
            given2=3,
            expected={
                1: {"multiplication": [1, 2, 3, 4, 5], "summation": [2, 3, 4, 5, 6]},
                2: {"multiplication": [2, 4, 6, 8, 10], "summation": [3, 4, 5, 6, 7]},
                3: {"multiplication": [3, 6, 9, 12, 15], "summation": [4, 5, 6, 7, 8]},
            },
        ),
        TestCase2(
            given1=10,
            given2=12,
            expected={
                10: {
                    "multiplication": [10, 20, 30, 40, 50],
                    "summation": [11, 12, 13, 14, 15],
                },
                11: {
                    "multiplication": [11, 22, 33, 44, 55],
                    "summation": [12, 13, 14, 15, 16],
                },
                12: {
                    "multiplication": [12, 24, 36, 48, 60],
                    "summation": [13, 14, 15, 16, 17],
                },
            },
        ),
        TestCase2(given1=10, given2=3, expected={0: 0}),
        TestCase2(given1=18, given2=18, expected={0: 0}),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=test_case.expected,
            actual=guide8(a=a, b=b),
        )
