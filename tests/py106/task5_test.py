import pytest

from src.py106.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask5:
    test_cases = [
        TestCase(given="UNCOPYRIGHTABLE", expected=True),
        TestCase(given="PUBVEXINGFJORD-SCHMALTZY", expected=True),
        TestCase(given="bilabial", expected=False),
        TestCase(given="SwedEn", expected=False),
        TestCase(given="", expected=False),
        TestCase(given=None, expected=False),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> word= {test_case.given}",
            expected=test_case.expected,
            actual=task5(test_case.given),
        )
