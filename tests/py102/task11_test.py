import pytest

from src.py102.task11 import task11
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask11:
    test_cases = [
        TestCase(given="MHFLMHH", expected="L"),
        TestCase(given="LMFHLFLMHFLMHHFLHLF", expected="H"),
        TestCase(given="MMHMFHFLMHHMFFL", expected="M"),
        TestCase(given="MHHFLHHMFLFMLFH", expected="F"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> assessments= {test_case.given}",
            expected=test_case.expected,
            actual=task11(test_case.given),
        )
