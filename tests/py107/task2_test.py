import pytest

from src.py107 import task2
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        TestCase(given=1, expected="Foo"),
        TestCase(given=6, expected="Fizz"),
        TestCase(given=10, expected="Buzz"),
        TestCase(given=15, expected="FizzBuzz"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task2
        function_name = "fizz"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        fizz = getattr(module, function_name)

        assert_equals(
            message=f"> number= {test_case.given}",
            expected=test_case.expected,
            actual=fizz(test_case.given),
        )
