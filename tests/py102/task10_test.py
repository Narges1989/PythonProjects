import pytest

from src.py102.task10 import task10
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask10:
    test_cases = [
        TestCase(given="MHFLMHH", expected=7),
        TestCase(given="LMFHLFLMHFLMHHFLHLF", expected=19),
        TestCase(given="MMHMFHFLMHHMFFL", expected=15),
        TestCase(given="MHHFLHHMFLFMLFH", expected=15),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> assessments= {test_case.given}",
            expected=test_case.expected,
            actual=task10(test_case.given),
        )
