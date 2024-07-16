import pytest

from src.py107 import guide8
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestGuide8:
    test_cases = [
        TestCase(given="abcd fgijk", expected=[]),
        TestCase(given="hhhh aaaaa", expected=[]),
        TestCase(given="H16dhas8HaoH", expected=[0, 8, 11]),
        TestCase(given="HHHHH", expected=[0, 1, 2, 3, 4]),
        TestCase(given="abhd HHHHH", expected=[5, 6, 7, 8, 9]),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = guide8
        function_name = "indexer"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        sentence = test_case.given
        indexer = getattr(module, function_name)

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=sorted(test_case.expected),
            actual=sorted(indexer(sentence)),
        )
