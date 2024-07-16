import pytest

from src.py107 import guide4
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase2


class TestGuide4:
    test_cases = [
        TestCase2(given1="", given2="", expected=[]),
        TestCase2(given1="abc", given2="abc", expected=["a", "b", "c"]),
        TestCase2(given1="abbbbc", given2="aabcccc", expected=["a", "b", "c"]),
        TestCase2(given1="xyyyyz", given2="XYzZZz", expected=["z"]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = guide4
        function_name = "equalizer"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 2),
        )

        text1 = test_case.given1
        text2 = test_case.given2
        equalizer = getattr(module, function_name)

        assert_equals(
            message=f"> text 1 = {text1}\n> text 2 = {text2}",
            expected=sorted(test_case.expected),
            actual=sorted(equalizer(text1, text2)),
        )
