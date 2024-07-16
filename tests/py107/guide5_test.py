import pytest

from src.py107 import guide5
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestGuide5:
    test_cases = [
        TestCase(given=1, expected="Winter"),
        TestCase(given=2, expected="Winter"),
        TestCase(given=3, expected="Spring"),
        TestCase(given=4, expected="Spring"),
        TestCase(given=5, expected="Spring"),
        TestCase(given=6, expected="Summer"),
        TestCase(given=7, expected="Summer"),
        TestCase(given=8, expected="Summer"),
        TestCase(given=9, expected="Fall"),
        TestCase(given=10, expected="Fall"),
        TestCase(given=11, expected="Fall"),
        TestCase(given=12, expected="Winter"),
        TestCase(given=13, expected="Error"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = guide5
        function_name = "indecisive"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        month = test_case.given
        indecisive = getattr(module, function_name)

        assert_equals(
            message=f"> month = {month}",
            expected=test_case.expected,
            actual=indecisive(month),
        )

    def test_no_input(self):
        module = guide5
        function_name = "indecisive"
        indecisive = getattr(module, function_name)

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        assert_equals(
            message="Error: Missing default value on parameter `month`",
            expected="Fall",
            actual=indecisive(),
        )
