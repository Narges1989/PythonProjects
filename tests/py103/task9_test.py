import pytest

from src.py103.task9 import task9
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        TestCase(given="0C", expected="32F"),
        TestCase(given="1c", expected="33F"),
        TestCase(given="-90C", expected="-130F"),
        TestCase(given="-30C", expected="-22F"),
        TestCase(given="0F", expected="-17C"),
        TestCase(given="-90F", expected="-67C"),
        TestCase(given="50F", expected="10C"),
        TestCase(given="20F", expected="-6C"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_almost_equals(
            message=f"> temperature= {test_case.given}",
            expected=test_case.expected,
            actual=task9(test_case.given),
        )
