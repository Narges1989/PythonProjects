import pytest

from src.py107 import task4
from tests.helper.custom_assertions import (
    assert_almost_equals,
    assert_function_signature,
)
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase2


class TestTask4:
    test_cases = [
        # given1 is washes per day, given2 is routine duration per month
        TestCase2(given1=5, given2=5, expected=262.50),
        TestCase2(given1=2, given2=3, expected=63.0),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task4
        function_name = "washing"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 2),
        )

        washes_per_day = test_case.given1
        routine_duration_in_months = test_case.given2

        washing = getattr(module, function_name)

        assert_almost_equals(
            message=f"> washes per day= {washes_per_day}\n> routine duration= {routine_duration_in_months}",
            expected=test_case.expected,
            actual=washing(washes_per_day, routine_duration_in_months),
        )
