import pytest

from src.py103.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask7:
    test_cases = [
        # given1 is a, given2 is b
        TestCase2(given1=18, given2=0, expected=1),
        TestCase2(given1=30, given2=0, expected=1),
        TestCase2(given1=50, given2=0, expected=1),
        TestCase2(given1=35, given2=0, expected=1),
        TestCase2(given1=5, given2=1, expected=5),
        TestCase2(given1=65, given2=1, expected=65),
        TestCase2(given1=17, given2=1, expected=17),
        TestCase2(given1=-5, given2=2, expected=25),
        TestCase2(given1=-2, given2=3, expected=-8),
        TestCase2(given1=2, given2=2, expected=4),
        TestCase2(given1=5, given2=3, expected=125),
        TestCase2(given1=9, given2=5, expected=59_049),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a= {a}\n> b= {b}",
            expected=test_case.expected,
            actual=task7(a, b),
        )
