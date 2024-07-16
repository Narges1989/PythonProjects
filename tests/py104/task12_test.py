import pytest

from src.py104.task12 import task12
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestTask12:
    attendees = [
        "ZZStéphanie-A",
        "ZZKù-A",
        "ZZÖrjan-A",
        "ZZPublicité-A",
        "ZZEdmée-K",
        "ZZMaëline-K",
        "ZZNaéva-K",
        "ZZUò-V",
        "ZZCloé-V",
        "ZZFèi-V",
        "ZZMélissandre-V",
        "ZZTáng-V",
        "ZZLéana-V",
    ]

    test_cases = [
        TestCase2(
            given1=attendees,
            given2="-A",
            expected=["ZZStéphanie-A", "ZZKù-A", "ZZÖrjan-A", "ZZPublicité-A"],
        ),
        TestCase2(
            given1=attendees,
            given2="-V",
            expected=[
                "ZZUò-V",
                "ZZCloé-V",
                "ZZFèi-V",
                "ZZMélissandre-V",
                "ZZTáng-V",
                "ZZLéana-V",
            ],
        ),
        TestCase2(
            given1=attendees,
            given2="-K",
            expected=["ZZEdmée-K", "ZZMaëline-K", "ZZNaéva-K"],
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> condition= {test_case.given2}\n> guests= {test_case.given1}",
            expected=test_case.expected,
            actual=task12(test_case.given1, test_case.given2),
        )
