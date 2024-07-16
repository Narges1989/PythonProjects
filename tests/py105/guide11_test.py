import pytest

from src.py105.guide11 import guide11
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide11:
    test_cases = [
        TestCase(given={}, expected=0.0),
        TestCase(given={"Patrik": 5.0}, expected=5.0),
        TestCase(given={"Far": 5.0, "Bob": 4.5, "Ben": 5.0}, expected=4.83),
        TestCase(given={"Far": 3.0, "Bob": 4.5, "Ben": 4.8}, expected=4.1),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given

        assert_almost_equals(
            message=f"> classroom = {classroom}",
            expected=test_case.expected,
            actual=guide11(classroom),
        )
