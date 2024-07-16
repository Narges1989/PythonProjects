import pytest

from src.py107 import task5
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature
from tests.helper.TestCase import TestCase


class TestTask5:
    test_cases = [
        TestCase(
            given=[],
            expected=0.0,
        ),
        TestCase(
            given=[
                {"product": "Milk", "quantity": 3, "price": 1.50},
                {"product": "Meat", "quantity": 2, "price": 2.50},
            ],
            expected=9.5,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        module = task5
        function_name = "groceries"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 1),
        )

        groceries = getattr(module, function_name)

        assert_equals(
            message=f"> Products= {test_case.given}",
            expected=test_case.expected,
            actual=groceries(test_case.given),
        )
