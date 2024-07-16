import pytest

from src.py105.task3 import task3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask3:
    test_cases = [
        TestCase2(
            given1={1: "A", 2: "B", 3: "C"},
            given2={1: "AA", 2: "BB", 4: "DD"},
            expected=[1, 2],
        ),
        TestCase2(
            given1={1: "A", 2: "B", 3: "C"},
            given2={4: "AA", 5: "BB", 6: "DD"},
            expected=[],
        ),
        TestCase2(
            given1={10: "A", 20: "B", 30: "C"},
            given2={10: "AA", 20: "BB", 40: "DD"},
            expected=[10, 20],
        ),
        TestCase2(
            given1={10: "A", 2: "B", 39: "C"},
            given2={10: "AA", 2: "BB", 39: "DD"},
            expected=[10, 2, 39],
        ),
        TestCase2(
            given1={-10: "A", -2: "B", -39: "C"},
            given2={-10: "AA", -2: "BB", -39: "DD"},
            expected=[-10, -2, -39],
        ),
        TestCase2(
            given1={-10: "A", 2: "B", -39: "C"},
            given2={-10: "AA", 2: "BB", 39: "DD"},
            expected=[-10, 2],
        ),
        TestCase2(
            given1={-10: "A", -2: "B", -39: "C"},
            given2={10: "AA", 2: "BB", 39: "DD"},
            expected=[],
        ),
        TestCase2(
            given1={},
            given2={},
            expected=[],
        ),
        TestCase2(
            given1={1: "A", 2: "B", 3: "C"},
            given2={},
            expected=[],
        ),
        TestCase2(
            given1={},
            given2={1: "A", 2: "B", 3: "C"},
            expected=[],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a= {a}\n> b= {b}",
            expected=sorted(test_case.expected),
            actual=sorted(task3(a, b)),
        )
