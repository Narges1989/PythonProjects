import pytest

from src.py107 import task8
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        TestCase(given="", expected=0),
        TestCase(given="N vwls hr", expected=0),
        TestCase(given="U", expected=1),
        TestCase(given="OO", expected=4),
        TestCase(given="iIi", expected=9),
        TestCase(given="I LOVE KOTLIN", expected=14),
        TestCase(given="I love kotlin", expected=14),
        TestCase(given="eEeE", expected=16),
        TestCase(given="aaAAa", expected=25),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task8
        function_name = "vowels"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        vowels = getattr(module, function_name)

        assert_equals(
            message=f"> text= {test_case.given}",
            expected=test_case.expected,
            actual=vowels(test_case.given),
        )
