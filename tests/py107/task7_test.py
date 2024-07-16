import pytest

from src.py107 import task7
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        TestCase(given="", expected=""),
        TestCase(given="I live in Sweden", expected="I live in ******"),
        TestCase(given="Avoid saying bad words", expected="***** ****** bad *****"),
        TestCase(given="I do not say bad wrds", expected="I do not say bad wrds"),
        TestCase(given="123 123 123 12345 12345", expected="123 123 123 ***** *****"),
        TestCase(given="12345 123 1234 12345 123", expected="***** 123 1234 ***** 123"),
        TestCase(
            given="Hello John, I live in Sweden",
            expected="***** John, I live in ******",
        ),
        TestCase(given="My name is: Kotlin", expected="My name is: ******"),
        TestCase(
            given="Hello 12345, I live in Sweden",
            expected="***** *****, I live in ******",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task7
        function_name = "censorship"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        censorship = getattr(module, function_name)

        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=censorship(test_case.given),
        )
