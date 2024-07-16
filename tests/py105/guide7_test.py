import pytest

from src.py105.guide7 import guide7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide7:
    test_cases = [
        TestCase(given={}, expected=0),
        TestCase(
            given={"Ann Lint": 10.0, "Pat Borg": 9.5, "Pat Lark": 9.0}, expected=0
        ),
        TestCase(given={"Ann Li": 10.0, "Pat Lee": 9.5, "Pat In": 9.0}, expected=0),
        TestCase(
            given={"Eric Ericsson": 9.5, "Ann Carlson": 10.0, "Thomas Edison": 9.0},
            expected=1,
        ),
        TestCase(
            given={"Ann Johannsson": 10.0, "Pat Ericsson": 9.5, "Pat Lark": 9.0},
            expected=2,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given

        assert_equals(
            message=f"> classroom = {classroom}",
            expected=test_case.expected,
            actual=guide7(classroom),
        )
