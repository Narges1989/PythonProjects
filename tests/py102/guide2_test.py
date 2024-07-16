import pytest

from src.py102.guide2 import guide2
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase2


class TestGuide2:
    test_cases = [
        # given 1 is base, given2 is height
        TestCase2(given1=5.0, given2=10.0, expected=25.0),
        TestCase2(given1=0.0, given2=0.0, expected=0.0),
        TestCase2(given1=3.1, given2=5.6, expected=8.68),
        TestCase2(given1=90.8, given2=11.56, expected=524.82),
        TestCase2(given1=3.56, given2=18.18, expected=32.36),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        base = test_case.given1
        height = test_case.given2

        assert_almost_equals(
            message=f"> base = {base}\n> height = {height}",
            expected=test_case.expected,
            actual=guide2(base=base, height=height),
        )
