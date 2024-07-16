import pytest

from src.py103.guide4 import guide4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide4:
    test_cases = [
        TestCase(given=0, expected=False),
        TestCase(given=1233, expected=False),
        TestCase(given=5679, expected=False),
        TestCase(given=3178, expected=False),
        TestCase(given=5678, expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        pin_code = test_case.given

        assert_equals(
            message=f"> code = {pin_code}",
            expected=test_case.expected,
            actual=guide4(pin=pin_code),
        )
