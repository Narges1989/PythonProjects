import pytest

from src.py106.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        TestCase(given=None, expected={"letters": 0, "digits": 0}),
        TestCase(given="", expected={"letters": 0, "digits": 0}),
        TestCase(given="12345 67890", expected={"letters": 0, "digits": 10}),
        TestCase(given="Hello World", expected={"letters": 10, "digits": 0}),
        TestCase(given="HEllO WORld", expected={"letters": 10, "digits": 0}),
        TestCase(given="H3ll0 Wor1d", expected={"letters": 7, "digits": 3}),
        TestCase(given="H3LL0 W0R1D", expected={"letters": 6, "digits": 4}),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task7(test_case.given),
        )
