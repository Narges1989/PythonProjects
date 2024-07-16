import pytest

from src.py105.guide12 import guide12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide12:
    test_cases = [
        TestCase(
            given={"cover-letter.pdf": 5.5, "paradise.png": 1.0, "report.pptx": 3.4},
            expected=9.9,
        ),
        TestCase(given={"cv.pdf": 5.5, "screen.png": 1.0, "app.py": 3.4}, expected=6.5),
        TestCase(
            given={"run.kt": 4.0, "cv.java": 5.5, "screen.json": 1.0, "app.py": 3.4},
            expected=0.0,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        hard_drive = test_case.given

        assert_equals(
            message=f"> hard drive = {hard_drive}",
            expected=test_case.expected,
            actual=guide12(hard_drive),
        )
