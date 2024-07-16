import pytest

from src.py105.guide16 import guide16
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide16:
    test_cases = [
        TestCase(given={}, expected={}),
        TestCase(
            given={"cv.pdf": 5.5, "screen.png": 1.0, "app.py": 3.4},
            expected={
                "cv.pdf": 0.00537109375,
                "screen.png": 0.0009765625,
                "app.py": 0.0033203125,
            },
        ),
        TestCase(
            given={"cover-Letter.pdf": 2.0, "paradise.png": 1.5, "Run.py": 2.2},
            expected={
                "cover-Letter.pdf": 0.001953125,
                "paradise.png": 0.00146484375,
                "Run.py": 0.0021484375,
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        hard_drive = test_case.given

        assert_almost_equals(
            message=f"> hard drive = {hard_drive}",
            expected=test_case.expected,
            actual=guide16(hard_drive),
        )
