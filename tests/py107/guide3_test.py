from src.py107 import guide3
from tests.helper.custom_assertions import assert_equals, assert_function_signature
from tests.helper.FunctionSignature import FunctionSignature


class TestGuide3:
    def test_task_grading(self):
        module = guide3
        function_name = "baldor"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 0),
        )

        baldor = getattr(module, function_name)

        assert_equals(
            message="-",
            expected=309136,
            actual=baldor(),
        )
