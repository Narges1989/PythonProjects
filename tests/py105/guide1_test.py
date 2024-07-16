import pytest

from src.py105.guide1 import guide1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide1:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1=1, given2=1, expected=dict()),
        TestCase2(given1=10, given2=1, expected=dict()),
        TestCase2(given1=1, given2=3, expected={1: 3, 2: 4, 3: 9}),
        TestCase2(given1=5, given2=8, expected={5: 15, 6: 12, 7: 21, 8: 16}),
        TestCase2(
            given1=-10,
            given2=-1,
            expected={
                -10: -20,
                -9: -27,
                -8: -16,
                -7: -21,
                -6: -12,
                -5: -15,
                -4: -8,
                -3: -9,
                -2: -4,
                -1: -3,
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=test_case.expected,
            actual=guide1(a=a, b=b),
        )
