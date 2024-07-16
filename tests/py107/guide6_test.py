import pytest

from src.py107 import guide6
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestGuide6:
    test_cases = [
        TestCase(given=tuple((1,)), expected=1),
        TestCase(given=tuple((1, 2)), expected=3),
        TestCase(given=tuple((15, 21)), expected=36),
        TestCase(given=tuple((11, 22, 44)), expected=77),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = guide6
        function_name = "summation"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        numbers = test_case.given
        summation = getattr(module, function_name)

        assert_equals(
            message=f"> numbers = {numbers}",
            expected=test_case.expected,
            actual=summation(*numbers),
        )
