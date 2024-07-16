import pytest

from src.py107 import task1
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask1:
    test_cases = [
        TestCase(given="", expected=""),
        TestCase(given="Hello", expected="Hll"),
        TestCase(given="HELLO", expected="HLL"),
        TestCase(given="Sweden is nice", expected="Swdn s nc"),
        TestCase(given="You Like Kotlin", expected="Y Lk Ktln"),
        TestCase(given="aeiouAEIUOH", expected="H"),
        TestCase(given="HlF NFb MlF", expected="HlF NFb MlF"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task1
        function_name = "remover"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        remover = getattr(module, function_name)

        assert_equals(
            message=f"> text= {test_case.given}",
            expected=test_case.expected,
            actual=remover(test_case.given),
        )
