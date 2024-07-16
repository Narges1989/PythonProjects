import pytest

from src.py107 import guide7
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestGuide7:
    test_cases = [
        TestCase(given=[], expected=[]),
        TestCase(given=[1, 2, 3], expected=[2, 3, 4]),
        TestCase(given=[10, 11, 12], expected=[11, 12, 13]),
        TestCase(given=[15, 23, 67], expected=[16, 24, 68]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = guide7
        function_name = "bonus"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        original = test_case.given
        bonus = getattr(module, function_name)

        bonus(original)

        assert_equals(
            message=f"> numbers = {original}",
            expected=test_case.expected,
            actual=original,
        )
