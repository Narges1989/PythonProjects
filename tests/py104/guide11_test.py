import pytest

from src.py104.guide11 import guide11
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide11:
    test_cases = [
        TestCase(
            given=[99, 78, 66, 55, 9, 10, 6, 11, 55],
            expected=[297, 78, 198, 165, 9, 10, 6, 33, 165],
        ),
        TestCase(
            given=[11, 12, 22, 23, 24, 33, 35, 77, 11],
            expected=[33, 12, 66, 23, 24, 99, 35, 231, 33],
        ),
        TestCase(
            given=[12, 14, 16, 17, 18, 20, 23], expected=[12, 14, 16, 17, 18, 20, 23]
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=sorted(test_case.expected),
            actual=sorted(guide11(items)),
        )
