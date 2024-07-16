import pytest

from src.py108 import guide2
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import assert_class_exists, assert_equals
from tests.helper.TestCase import TestCase


class TestGuide2:
    test_cases = [
        TestCase(given=1, expected="Pizza.SMALL"),
        TestCase(given=3, expected="Pizza.SMALL"),
        TestCase(given=4, expected="Pizza.MEDIUM"),
        TestCase(given=6, expected="Pizza.MEDIUM"),
        TestCase(given=7, expected="Pizza.LARGE"),
        TestCase(given=9, expected="Pizza.LARGE"),
        TestCase(given=10, expected="Pizza.FAMILY"),
        TestCase(given=12, expected="Pizza.FAMILY"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        self.__assert_class_exists()

        attendees = test_case.given

        assert_equals(
            message=f"> attendees = {attendees}",
            expected=test_case.expected,
            actual=str(guide2.guide2(attendees=attendees)),
        )

    def __assert_class_exists(self):
        module = guide2
        class_name = "Pizza"

        assert_class_exists(module=module, class_name=class_name)
