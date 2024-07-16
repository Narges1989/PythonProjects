import pytest

from src.py102.guide1 import guide1
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase3


class TestGuide1:
    test_cases = [
        # given1 is length, given2 is width, given3 is height
        TestCase3(given1=5.0, given2=10.0, given3=10.0, expected=500.0),
        TestCase3(given1=0.0, given2=0.0, given3=0.0, expected=0.0),
        TestCase3(given1=12.5, given2=11.67, given3=33.78, expected=4927.65),
        TestCase3(given1=13.9, given2=4.1, given3=1.56, expected=88.9044),
        TestCase3(given1=1.9, given2=2.1, given3=3.0, expected=11.97),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        length = test_case.given1
        width = test_case.given2
        height = test_case.given3

        assert_almost_equals(
            message=f"> length= {length}\n> width= {width}\n> height = {height}",
            expected=test_case.expected,
            actual=guide1(length=length, width=width, height=height),
        )
