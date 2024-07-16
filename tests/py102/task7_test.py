import pytest

from src.py102.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        TestCase(given="", expected=0),
        TestCase(given="H", expected=1),
        TestCase(given="Hello World", expected=11),
        TestCase(given="Sweden is beautiful", expected=19),
        TestCase(given="I love Kotlin", expected=13),
        TestCase(given="Android is better than iOS", expected=26),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task7(test_case.given),
        )
