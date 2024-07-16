import pytest

from src.py107 import task3
from tests.helper.custom_assertions import (
    assert_almost_equals,
    assert_function_signature,
)
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        TestCase(given=5, expected=18_000_000),
        TestCase(given=10, expected=36_000_000),
        TestCase(given=15, expected=54_000_000),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task3
        function_name = "converter"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        converter = getattr(module, function_name)

        assert_almost_equals(
            message=f"> hours= {test_case.given}",
            expected=test_case.expected,
            actual=converter(test_case.given),
        )
