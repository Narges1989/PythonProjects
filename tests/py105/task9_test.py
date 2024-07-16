import pytest

from src.py105.task9 import task9
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        TestCase(
            given={},
            expected=0.0,
        ),
        TestCase(
            given={"Ana": [4.0, 4.5, 5.0]},
            expected=4.5,
        ),
        TestCase(
            given={"Ana": [0.0, 0.5, 0.0]},
            expected=0.166666,
        ),
        TestCase(
            given={
                "Ana": [4.0, 4.5, 5.0],
                "John": [5.0, 5.0, 3.0],
                "Lise": [5.0, 5.0, 5.0],
            },
            expected=4.6111,
        ),
        TestCase(
            given={
                "Ana": [3.9, 2.5, 2.5],
                "John": [4.3, 4.2, 4.7],
                "Lise": [4.2, 4.3, 4.4],
            },
            expected=3.88888,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_almost_equals(
            message=f"> grades= {test_case.given}",
            expected=test_case.expected,
            actual=task9(test_case.given),
        )
