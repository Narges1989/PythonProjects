import pytest

from src.py105.guide17 import guide17
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide17:
    test_cases = [
        TestCase(
            given={
                "history": {"enrolled": 30, "days": 3},
                "programming": {"enrolled": 100, "days": 5},
                "physics": {"enrolled": 80, "days": 2},
            },
            expected="programming",
        ),
        TestCase(
            given={
                "math": {"enrolled": 20, "days": 2},
            },
            expected="math",
        ),
        TestCase(
            given={
                "chemistry": {"enrolled": 50, "days": 3},
                "geography": {"enrolled": 10, "days": 5},
                "math": {"enrolled": 8, "days": 2},
            },
            expected="chemistry",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        education = test_case.given

        assert_equals(
            message=f"> education = {education}",
            expected=test_case.expected,
            actual=guide17(education),
        )
