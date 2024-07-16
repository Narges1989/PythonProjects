import pytest

from src.py106.task10 import task10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask10:
    test_cases = [
        TestCase(given=["Nemo", "NEMO", "nemo", "nEMO"], expected=0),
        TestCase(given=["Maybe", "you", None, "Nemo", "find", None], expected=3),
        TestCase(given=["I", "cannot", "Nemo", "find", "him"], expected=2),
        TestCase(given=[], expected=None),
        TestCase(given=[None, None, None], expected=None),
        TestCase(given=["I", "cannot", "find", "him"], expected=None),
        TestCase(given=["This", "NEMO", "is", "A", "fake", "nemo"], expected=None),
        TestCase(given=[None, "NEMO", "nemo", "nEMO"], expected=None),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> items= {test_case.given}",
            expected=test_case.expected,
            actual=task10(test_case.given),
        )
