import pytest

from src.py105.guide20 import guide20
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide20:
    test_cases = [
        TestCase(
            given={
                "app": {"size": 9.3, "extension": "py"},
            },
            expected="py",
        ),
        TestCase(
            given={
                "cover": {"size": 9.3, "extension": "py"},
                "main": {"size": 1.1, "extension": "kt"},
                "run": {"size": 2.9, "extension": "pdf"},
            },
            expected="kt",
        ),
        TestCase(
            given={
                "cover": {"size": 9.3, "extension": "py"},
                "main": {"size": 4.1, "extension": "kt"},
                "run": {"size": 2.9, "extension": "pdf"},
            },
            expected="pdf",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        hard_drive = test_case.given

        assert_equals(
            message=f"> hard drive = {hard_drive}",
            expected=test_case.expected,
            actual=guide20(hard_drive),
        )
