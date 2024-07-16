import pytest

from src.py107 import task6
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask6:
    test_cases = [
        # "AlExa" --> 1 + 12 + 5 + 24 + 1 --> 43
        # "MauRi" --> 13 + 1 + 21 + 18 + 9 --> 62
        TestCase(given="AlExa MauRi", expected=False),
        TestCase(given="alexa mauri", expected=False),
        TestCase(given="ALEXa", expected=False),
        TestCase(given="alexa", expected=False),
        TestCase(given="MaUrI", expected=True),
        TestCase(given="mauri", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task6
        function_name = "counter"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        counter = getattr(module, function_name)

        assert_equals(
            message=f"> text= {test_case.given}",
            expected=test_case.expected,
            actual=counter(test_case.given),
        )
