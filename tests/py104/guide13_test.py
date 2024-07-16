import pytest

from src.py104.guide13 import guide13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide13:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(given1="Peru", given2="England", expected=[]),
        TestCase2(given1="Norway", given2="China", expected=["a"]),
        TestCase2(given1="Panama", given2="Sweden", expected=["n"]),
        TestCase2(given1="Sweden", given2="SPAIN", expected=["S"]),
        TestCase2(given1="sweden", given2="spain", expected=["s", "n"]),
        TestCase2(given1="India", given2="China", expected=["n", "i", "a"]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=sorted(test_case.expected),
            actual=sorted(guide13(a=a, b=b)),
        )
