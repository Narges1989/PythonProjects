from src.py107 import guide2
from tests.helper.custom_assertions import assert_function_signature, assert_printed
from tests.helper.FunctionSignature import FunctionSignature


class TestGuide2:
    def test_task_grading(self, capfd):
        module = guide2
        function_name = "exponential"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 0),
        )

        exponential = getattr(module, function_name)
        exponential()

        assert_printed(
            message="-",
            expected="336600",
            pattern="336600",
            capfd=capfd,
        )
