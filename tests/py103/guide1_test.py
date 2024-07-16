import pytest

from src.py103.guide1 import guide1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide1:
    test_cases = [
        TestCase(given="Panama", expected=False),
        TestCase(given="PANAMA", expected=False),
        TestCase(given="Norway", expected=False),
        TestCase(given="NorWaY", expected=False),
        TestCase(given="Sweden", expected=True),
        TestCase(given="sweden", expected=True),
        TestCase(given="SWEDEN", expected=True),
        TestCase(given="SwEdEn", expected=True),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        country = test_case.given

        assert_equals(
            message=f"> country = {country}",
            expected=test_case.expected,
            actual=guide1(country=country),
        )
