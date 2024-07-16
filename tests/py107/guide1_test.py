from src.py107 import guide1
from tests.helper.custom_assertions import assert_function_signature, assert_printed
from tests.helper.FunctionSignature import FunctionSignature


class TestGuide1:
    def test_task_grading(self, capfd):
        module = guide1
        function_name = "multiplication"

        assert_function_signature(
            module=module,
            function_signature=FunctionSignature(function_name, 0),
        )

        multiplication = getattr(module, function_name)
        multiplication()

        assert_printed(
            message="-",
            expected="945",
            pattern="945",
            capfd=capfd,
        )
