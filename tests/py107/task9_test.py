import pytest

from src.py107 import task9
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        TestCase(given=1, expected=True),
        TestCase(given=8, expected=True),
        TestCase(given=45, expected=True),
        TestCase(given=114, expected=True),
        TestCase(given=1729, expected=True),
        TestCase(given=0, expected=False),
        TestCase(given=19, expected=False),
        TestCase(given=44, expected=False),
        TestCase(given=115, expected=False),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task9
        function_name = "harshad"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        harshad = getattr(module, function_name)

        assert_equals(
            message=f"> number= {test_case.given}",
            expected=test_case.expected,
            actual=harshad(test_case.given),
        )
