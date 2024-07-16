import pytest

from src.py105.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask5:
    test_cases = [
        TestCase2(
            given1={},
            given2=0,
            expected=[],
        ),
        TestCase2(
            given1={1: 10},
            given2=10,
            expected=[],
        ),
        TestCase2(
            given1={1: 10},
            given2=0,
            expected=[1],
        ),
        TestCase2(
            given1={1: 10, 2: 20, 3: 30, 4: 20, 15: 10, 100: 30},
            given2=20,
            expected=[1, 3, 15, 100],
        ),
        TestCase2(
            given1={1: 10, 2: 10, 3: 10, 4: 10, 15: 10, 100: 10},
            given2=10,
            expected=[],
        ),
        TestCase2(
            given1={-10: 87, -1: 200, -2: 200, -20: 122, -3: 87},
            given2=200,
            expected=[-10, -20, -3],
        ),
        TestCase2(
            given1={-10: 87, -1: 87, -2: 87, -20: 87, -3: 87},
            given2=87,
            expected=[],
        ),
        TestCase2(
            given1={1: 100, 2: 100, 3: 100, 4: 100, 5: 100},
            given2=0,
            expected=[1, 2, 3, 4, 5],
        ),
        TestCase2(
            given1={1: 100, 2: 100, 3: 100, 4: 100, 5: 100},
            given2=100,
            expected=[],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> mapa= {test_case.given1}\n> constant= {test_case.given2}",
            expected=sorted(test_case.expected),
            actual=sorted(task5(test_case.given1, test_case.given2)),
        )
