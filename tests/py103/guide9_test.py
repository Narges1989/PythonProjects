import pytest

from src.py103.guide9 import guide9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide9:
    test_cases = [
        TestCase(given="humberto@programming.se", expected=True),
        TestCase(given="python@python.se", expected=True),
        TestCase(given="python@code.se", expected=True),
        TestCase(given="", expected=False),  # it is empty
        TestCase(given="hellolinerotech.se", expected=False),  # does not contain the @
        TestCase(
            given="hello@linerotech.com", expected=False
        ),  # does not finish in .se
        TestCase(given="hello@linerotech.", expected=False),  # missing tld
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        email = test_case.given

        assert_equals(
            message=f"> email = {email}",
            expected=test_case.expected,
            actual=guide9(email=email),
        )
