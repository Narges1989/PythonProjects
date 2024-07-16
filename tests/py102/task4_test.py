import pytest

from src.py102.task4 import task4
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase2


class TestTask4:
    test_cases = [
        # input1 is base, input2 is height
        TestCase2(given1=10.0, given2=10.0, expected=50.0),
        TestCase2(given1=0.0, given2=10.0, expected=0.0),
        TestCase2(given1=5.0, given2=10.0, expected=25.0),
        TestCase2(given1=25.2, given2=23.6, expected=297.36),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        base = test_case.given1
        height = test_case.given2

        assert_almost_equals(
            message=f"> base= {base}\n> height= {height}",
            expected=test_case.expected,
            actual=task4(base, height),
        )
