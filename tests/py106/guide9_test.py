import pytest

from src.py106.guide9 import guide9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide9:
    test_cases = [
        TestCase(
            given={
                "Petter": {
                    "student-id": 1234,
                    "grades": [4.0, 5.0, None, 4.4, None, 5.0, 5.0],
                },
                "Johan": {
                    "student-id": 4563,
                    "grades": [3.0, None, 3.3, 5.0, None, None, 5.0],
                },
                "Handra": {
                    "student-id": 7584,
                    "grades": [None, 3.0, None, 4.4, None, 4.0, 4.3],
                },
            },
            expected={
                "Petter": {
                    "student-id": 1234,
                    "grades": [4.0, 5.0, 0.0, 4.4, 0.0, 5.0, 5.0],
                },
                "Johan": {
                    "student-id": 4563,
                    "grades": [3.0, 0.0, 3.3, 5.0, 0.0, 0.0, 5.0],
                },
                "Handra": {
                    "student-id": 7584,
                    "grades": [0.0, 3.0, 0.0, 4.4, 0.0, 4.0, 4.3],
                },
            },
        ),
        TestCase(
            given={
                "Jendric": {
                    "student-id": 74,
                    "grades": [None, 5.0, 3.5, 4.4, 4.4, None, 5.0],
                },
                "Beth": {
                    "student-id": 23,
                    "grades": [None, None, None, None, None, None],
                },
                "Hugo": {"student-id": 23, "grades": [3.4, 5.0, 4.0, 3.0, 2.0, 2.2]},
                "Mir": {
                    "student-id": 543,
                    "grades": [None, 3.0, None, 4.4, None, 4.0, 4.3],
                },
                "Hanna": {
                    "student-id": 23,
                    "grades": [
                        3.0,
                        None,
                        4.4,
                        None,
                        4.0,
                        4.3,
                        5.0,
                        None,
                        4.6,
                        None,
                        None,
                    ],
                },
                "Henrik": {
                    "student-id": 12,
                    "grades": [
                        None,
                        4.0,
                        None,
                        2.4,
                        None,
                        3.0,
                        3.5,
                        3.4,
                        3.5,
                        3.3,
                        4.4,
                    ],
                },
                "Helmut": {
                    "student-id": 36,
                    "grades": [
                        None,
                        3.0,
                        None,
                        4.4,
                        None,
                        4.0,
                        4.3,
                        None,
                        None,
                        None,
                        None,
                    ],
                },
            },
            expected={
                "Jendric": {
                    "student-id": 74,
                    "grades": [0.0, 5.0, 3.5, 4.4, 4.4, 0.0, 5.0],
                },
                "Beth": {"student-id": 23, "grades": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
                "Hugo": {"student-id": 23, "grades": [3.4, 5.0, 4.0, 3.0, 2.0, 2.2]},
                "Mir": {
                    "student-id": 543,
                    "grades": [0.0, 3.0, 0.0, 4.4, 0.0, 4.0, 4.3],
                },
                "Hanna": {
                    "student-id": 23,
                    "grades": [3.0, 0.0, 4.4, 0.0, 4.0, 4.3, 5.0, 0.0, 4.6, 0.0, 0.0],
                },
                "Henrik": {
                    "student-id": 12,
                    "grades": [0.0, 4.0, 0.0, 2.4, 0.0, 3.0, 3.5, 3.4, 3.5, 3.3, 4.4],
                },
                "Helmut": {
                    "student-id": 36,
                    "grades": [0.0, 3.0, 0.0, 4.4, 0.0, 4.0, 4.3, 0.0, 0.0, 0.0, 0.0],
                },
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given

        assert_equals(
            message=f"> classroom = {classroom}",
            expected=test_case.expected,
            actual=guide9(classroom=classroom),
        )
