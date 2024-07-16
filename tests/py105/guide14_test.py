import pytest

from src.py105.guide14 import guide14
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide14:
    test_cases = [
        TestCase(given={}, expected={}),
        TestCase(
            given={"Panama": "es", "Colombia": "es", "Spain": "es", "Costa Rica": "es"},
            expected={},
        ),
        TestCase(
            given={"Panama": "es", "Colombia": "es", "Spain": "es", "Denmark": "de"},
            expected={"Denmark": "de"},
        ),
        TestCase(
            given={"Panama": "es", "Sweden": "sv", "Spain": "es", "Denmark": "da"},
            expected={"Sweden": "sv", "Denmark": "da"},
        ),
        TestCase(
            given={"Iceland": "ic", "Sweden": "sv", "Norway": "no", "Denmark": "da"},
            expected={"Iceland": "ic", "Sweden": "sv", "Norway": "no", "Denmark": "da"},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        scandinavia = test_case.given

        assert_equals(
            message=f"> scandinavia = {scandinavia}",
            expected=test_case.expected,
            actual=guide14(scandinavia),
        )
