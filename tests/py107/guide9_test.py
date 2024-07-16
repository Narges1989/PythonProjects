import pytest

from src.py107 import guide9
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestGuide9:
    test_cases = [
        TestCase(given="", expected=""),
        TestCase(given="ABCDE", expected="$BCD$"),
        TestCase(given="abcde", expected="$bcd$"),
        TestCase(given="xyz ajeiy oju", expected="xyz $j$$y $j$"),
        TestCase(given="pty A E ljhg O o U", expected="pty $ $ ljhg $ $ $"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = guide9
        function_name = "transformer"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        sentence = test_case.given
        transformer = getattr(module, function_name)

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=test_case.expected,
            actual=transformer(sentence),
        )
