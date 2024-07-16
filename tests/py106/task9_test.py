import pytest

from src.py106.task9 import task9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        TestCase(given="19470110-1739", expected=True),
        TestCase(given="20001010-1847", expected=True),
        TestCase(given="20200331-7896", expected=True),
        TestCase(given="19991111-9038", expected=True),
        TestCase(given="19501212-8749", expected=True),
        TestCase(given="19920101-8749", expected=True),
        TestCase(given=None, expected=False),
        TestCase(given="", expected=False),
        TestCase(given=" ", expected=False),
        TestCase(given="ab", expected=False),
        TestCase(given="abcd1118-1984", expected=False),  # Invalid year
        TestCase(given="19460511-1084", expected=False),  # Invalid year
        TestCase(given="20000009-1233", expected=False),  # Invalid month
        TestCase(given="19951810-1743", expected=False),  # Invalid month
        TestCase(given="1995ab10-1743", expected=False),  # Invalid month
        TestCase(given="20200780-9473", expected=False),  # Invalid day
        TestCase(given="20200700-9473", expected=False),  # Invalid day
        TestCase(given="198006AB-7393", expected=False),  # Invalid day
        TestCase(given="991112-1839", expected=False),  # Invalid format
        TestCase(given="202011111876", expected=False),  # Invalid format
        TestCase(given="1992-11-11-1765", expected=False),  # Invalid format
        TestCase(given="19921111-abcd", expected=False),  # Invalid last four
        TestCase(given="19921111-ab01", expected=False),  # Invalid last four
        TestCase(given="19921111-11ab", expected=False),  # Invalid last four
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> identification= {test_case.given}",
            expected=test_case.expected,
            actual=task9(test_case.given),
        )
