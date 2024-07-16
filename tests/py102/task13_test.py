import pytest

from src.py102.task13 import task13
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask13:
    test_cases = [
        TestCase(given="MHFLMHH", expected="MHF"),
        TestCase(given="LMFHLFLMHFLMHHFLHLF", expected="LMF"),
        TestCase(given="MMHMFHFLMHHMFFL", expected="MMH"),
        TestCase(given="MHHFLHHMFLFMLFH", expected="MHH"),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> assessments= {test_case.given}",
            expected=test_case.expected,
            actual=task13(test_case.given),
        )
