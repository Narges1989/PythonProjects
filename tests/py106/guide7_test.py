import pytest

from src.py106.guide7 import guide7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide7:
    test_cases = [
        TestCase(
            given={
                "John": {
                    "grade": 9.3,
                    "classes": ["Math", "Chemistry", None, "Programming"],
                },
                "James": {
                    "grade": 9.3,
                    "classes": ["Music", "History", None, None, "Algebra"],
                },
                "Jane": {"grade": 4.1, "classes": [None, None, None]},
            },
            expected={
                "John": {"grade": 9.3, "classes": ["MaTh", "ChEmIsTrY", "PrOgRaMmInG"]},
                "James": {"grade": 9.3, "classes": ["MuSiC", "HiStOrY", "AlGeBrA"]},
                "Jane": {"grade": 4.1, "classes": []},
            },
        ),
        TestCase(
            given={
                "Haland": {
                    "grade": 10.1,
                    "classes": [
                        "Math",
                        "Chemistry",
                        None,
                        "History",
                        None,
                        "Programming",
                    ],
                },
                "Leo": {
                    "grade": 7.8,
                    "classes": ["Music", None, "Algebra", "Programming"],
                },
                "Lima": {"grade": 9.7, "classes": [None, None, None]},
                "Lenta": {"grade": 9.7, "classes": [None, None, None, None]},
            },
            expected={
                "Haland": {
                    "grade": 10.1,
                    "classes": ["MaTh", "ChEmIsTrY", "HiStOrY", "PrOgRaMmInG"],
                },
                "Leo": {"grade": 7.8, "classes": ["MuSiC", "AlGeBrA", "PrOgRaMmInG"]},
                "Lima": {"grade": 9.7, "classes": []},
                "Lenta": {"grade": 9.7, "classes": []},
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given

        assert_equals(
            message=f"> classroom = {classroom}",
            expected=test_case.expected,
            actual=guide7(classroom=classroom),
        )
