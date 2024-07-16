import pytest

from src.py102.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask5:
    test_cases = [
        # given1 is a, given2 is b
        TestCase2(given1=1, given2=3, expected=(3, 1)),
        TestCase2(given1=1, given2=2, expected=(2, 1)),
        TestCase2(given1=-1, given2=-2, expected=(-2, -1)),
        TestCase2(given1=-1, given2=2, expected=(2, -1)),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a= {a}\n> b= {b}",
            actual=task5(value_for_a=a, value_for_b=b),
            expected=test_case.expected,
        )
