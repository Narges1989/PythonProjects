import pytest

from src.py106.guide6 import guide6
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide6:
    test_cases = [
        TestCase(
            given={
                "Sweden": {"population": 10.42, "capital": "Stockholm"},
                "Norway": {"population": 5.4, "capital": "Oslo"},
                "Finland": {"population": 5.5, "capital": "Helsinki"},
            },
            expected=21.32,
        ),
        TestCase(
            given={
                "Sweden": {"population": 10.42, "capital": "Stockholm"},
                "Norway": {"population": 5.4, "capital": "Oslo"},
                "Finland": {"population": 5.5, "capital": "Helsinki"},
                "Denmark": {"population": 5.8, "capital": "Copenhagen"},
            },
            expected=27.12,
        ),
        TestCase(
            given={
                "Sweden": {"population": 10.42, "capital": "Stockholm"},
                "Norway": {"population": 5.4, "capital": "Oslo"},
                "Finland": {"population": 5.5, "capital": "Helsinki"},
                "Denmark": {"population": 5.8, "capital": "Copenhagen"},
            },
            expected=27.12,
        ),
        TestCase(
            given={
                "Sweden": {"population": 10.42, "capital": "Stockholm"},
                "Norway": {"population": 5.4, "capital": "Oslo"},
            },
            expected=15.82,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        scandinavia = test_case.given

        assert_almost_equals(
            message=f"> Scandinavia = {scandinavia}",
            expected=test_case.expected,
            actual=guide6(scandinavia=scandinavia),
        )

    failing_test_cases = [
        {
            "Sweden": {"population": 10.42, "capital": "Stockholm"},
            "Norway": {"population": 5.4, "capital": "Oslo"},
            "Panama": {"population": 4.3, "capital": "Panama"},
        },
        {
            "Sweden": {"population": 10.42, "capital": "Stockholm"},
            "Panama": {"population": 4.3, "capital": "Panama"},
            "Colombia": {"population": 51.5, "capital": "Bogota"},
        },
        {
            "Panama": {"population": 4.3, "capital": "Panama"},
            "Costa Rica": {"population": 5.1, "capital": "San José"},
            "Colombia": {"population": 51.5, "capital": "Bogota"},
            "Norway": {"population": 5.4, "capital": "Oslo"},
        },
    ]

    @pytest.mark.parametrize("failing_test_case", failing_test_cases)
    def test_failing_scenario(self, failing_test_case):
        with pytest.raises(AssertionError):
            guide6(scandinavia=failing_test_case)
