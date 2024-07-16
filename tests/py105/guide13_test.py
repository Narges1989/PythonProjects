import pytest

from src.py105.guide13 import guide13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide13:
    test_cases = [
        TestCase2(given1={}, given2="", expected={}),
        TestCase2(
            given1={"cv.pdf": 5.5, "screen.png": 1.0, "app.py": 3.4},
            given2="screen.png",
            expected={"cv.pdf": 5.5, "app.py": 3.4},
        ),
        TestCase2(
            given1={"cv.pdf": 5.5, "screen.png": 1.0, "Screen.png": 4.4, "app.py": 3.4},
            given2="screen.png",
            expected={"cv.pdf": 5.5, "Screen.png": 4.4, "app.py": 3.4},
        ),
        TestCase2(
            given1={
                "cv.pdf": 5.5,
                "cv.txt": 5.5,
                "screen.png": 1.0,
                "Screen.png": 4.4,
                "app.py": 3.4,
            },
            given2="cv.pdf",
            expected={
                "cv.txt": 5.5,
                "screen.png": 1.0,
                "Screen.png": 4.4,
                "app.py": 3.4,
            },
        ),
        TestCase2(
            given1={"cv.pdf": 5.5, "screen.png": 1.0, "Screen.png": 4.4, "app.py": 3.4},
            given2="cv.png",
            expected={
                "cv.pdf": 5.5,
                "screen.png": 1.0,
                "Screen.png": 4.4,
                "app.py": 3.4,
            },
        ),
        TestCase2(
            given1={"cv.pdf": 5.5, "screen.png": 1.0, "Screen.png": 4.4, "app.py": 3.4},
            given2="image.docx",
            expected={
                "cv.pdf": 5.5,
                "screen.png": 1.0,
                "Screen.png": 4.4,
                "app.py": 3.4,
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        hard_drive = test_case.given1
        corrupted = test_case.given2

        assert_equals(
            message=f"> hard drive = {hard_drive}\n> corrupted file = {corrupted}",
            expected=test_case.expected,
            actual=guide13(hard_drive, corrupted),
        )
