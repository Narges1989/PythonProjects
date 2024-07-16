import pytest

from src.py102.task12 import task12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask12:
    test_cases = [
        TestCase(given="MHFLMHH", expected="L"),
        TestCase(given="LMFHLFLMHFLMHHFLHLF", expected="F"),
        TestCase(given="MMHMFHFLMHHMFFL", expected="L"),
        TestCase(given="MHHFLHHMFLFMLFH", expected="M"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> assessments= {test_case.given}",
            expected=test_case.expected,
            actual=task12(test_case.given),
        )
