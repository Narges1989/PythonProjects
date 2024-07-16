import pytest

from src.py104.guide17 import guide17
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide17:
    test_cases = [
        TestCase(
            given=["cv.pdf", "screenshot.png", "app.jpeg", "main.docx", "thesis.pptx"],
            expected=[],
        ),
        TestCase(
            given=["py.pdf", "kt.png", "yml.jpeg", "json.docx", "java.pptx"],
            expected=[],
        ),
        TestCase(
            given=["app.yml", "app.md", "source.html"],
            expected=["app.yml"],
        ),
        TestCase(
            given=["python.pi", "weather.json", "script.py", "ios.ky"],
            expected=["weather.json", "script.py"],
        ),
        TestCase(
            given=[
                "python.PY",
                "management.kt",
                "result.json",
                "weather.JSON",
                "source.py",
            ],
            expected=[
                "management.kt",
                "result.json",
                "source.py",
            ],
        ),
        TestCase(
            given=[
                "portfolio.kt",
                "portfolio.png",
                "script.py",
                "run.py",
                "presentation.pptx",
                "app.java",
            ],
            expected=[
                "portfolio.kt",
                "script.py",
                "run.py",
                "app.java",
            ],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=test_case.expected,
            actual=guide17(items),
        )
