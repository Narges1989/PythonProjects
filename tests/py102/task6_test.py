import pytest

from src.py102.task6 import task6
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase3


class TestTask6:
    test_cases = [
        # given1 is base1, given2 is base2, given3 is height
        TestCase3(given1=10.0, given2=1.0, given3=1.0, expected=5.5),
        TestCase3(given1=5.0, given2=6.0, given3=10.0, expected=55.0),
        TestCase3(given1=0.0, given2=10.0, given3=1.9, expected=9.5),
        TestCase3(given1=1.0, given2=1.0, given3=0.0, expected=0.0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        base1 = test_case.given1
        base2 = test_case.given2
        height = test_case.given3

        assert_almost_equals(
            message=f"> base 1= {base1}\n> base 2= {base2}\n> height= {height}",
            actual=task6(base1, base2, height),
            expected=test_case.expected,
        )
