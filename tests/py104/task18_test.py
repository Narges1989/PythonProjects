import pytest

from src.py104.task18 import task18
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask18:
    test_cases = [
        TestCase(
            given=[
                "zzlmacro1i@360z.cn",
                "zzarichten1j@seesaaz.net",
                "zzmflawn1k@wundergroundz.com",
            ],
            expected=["360z", "seesaaz", "wundergroundz"],
        ),
        TestCase(
            given=[
                "zzcdalli1w@ftz.com",
                "zzrclayborn1x@mtvz.com",
                "zzrclayborn1x@mtvz.com",
                "zzjchidlow1y@nasaz.gov",
                "zzjchidlow1y@nasaz.gov",
                "zzkovell1z@washingtonpostz.com",
                "zzkovell1z@washingtonpostz.com",
            ],
            expected=["ftz", "mtvz", "nasaz", "washingtonpostz"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> customers= {test_case.given}",
            expected=sorted(test_case.expected),
            actual=sorted(task18(test_case.given)),
        )
