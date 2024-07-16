import pytest

from src.py105.task13 import task13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask13:
    test_cases = [
        TestCase(given="This is not a very very very small text", expected="very"),
        TestCase(given="this This THIS is still the very very same", expected="this"),
        TestCase(
            given="this, This; THIS, is still the very very same", expected="this"
        ),
        TestCase(given="word", expected="word"),
        TestCase(
            given="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor Lorem "
            + "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
            + "nostrud exercitation Lorem ullamco laboris nisi ut aliquip ex ea commodo consequat. "
            + "Lorem Duis aute irure dolor in reprehenderit in voluptate velit esse Lorem cillum dolore"
            + " eu fugiat nulla pariatur. Excepteur sint Lorem occaecat cupidatat non proident, sunt "
            + "in culpa qui officia deserunt mollit anim id est laborum.",
            expected="lorem",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> sentence= {test_case.given}",
            expected=test_case.expected,
            actual=task13(test_case.given),
        )
