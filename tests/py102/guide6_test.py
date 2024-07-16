import pytest

from src.py102.guide6 import guide6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide6:
    test_cases = [
        # given1 is firstname and given2 is the lastname
        TestCase2(
            given1="Humberto",
            given2="Linero",
            expected="Hello Humberto Linero. Welcome to programming",
        ),
        TestCase2(
            given1="John",
            given2="Svensson",
            expected="Hello John Svensson. Welcome to programming",
        ),
        TestCase2(
            given1="Jane",
            given2="Doe",
            expected="Hello Jane Doe. Welcome to programming",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        firstname = test_case.given1
        lastname = test_case.given2

        assert_equals(
            message=f"> firstname = {firstname}\n> lastname = {lastname}",
            expected=test_case.expected,
            actual=guide6(firstname=firstname, lastname=lastname),
        )
