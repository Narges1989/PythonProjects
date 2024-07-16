import pytest

from src.py105.task12 import task12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask12:
    test_cases = [
        TestCase2(
            given1=[1, 2, 3, 4],
            given2=["W", "X", "Y", "Z"],
            expected={1: "W", 2: "X", 3: "Y", 4: "Z"},
        ),
        TestCase2(
            given1=[5, 6, 7, 8],
            given2=["A", "B", "C", "D"],
            expected={5: "A", 6: "B", 7: "C", 8: "D"},
        ),
        TestCase2(
            given1=[10],
            given2=["Z"],
            expected={10: "Z"},
        ),
        TestCase2(
            given1=[-1, -2],
            given2=["-1", "-2"],
            expected={-1: "-1", -2: "-2"},
        ),
        TestCase2(
            given1=[],
            given2=[],
            expected={},
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> a= {test_case.given1}\n> b= {test_case.given2}",
            expected=test_case.expected,
            actual=task12(test_case.given1, test_case.given2),
        )
