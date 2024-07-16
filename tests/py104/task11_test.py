import pytest

from src.py104.task11 import task11
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask11:
    test_cases = [
        TestCase(
            given=[
                "ZZStéphanie-A",
                "ZZPublicité-A",
                "ZZKù-A",
                "ZZAdélaïde-A",
                "ZZÖrjan-A",
            ],
            expected=5,
        ),
        TestCase(
            given=["ZZEdmée-K", "ZZMaëlla-K", "ZZOcéanne-K"],
            expected=3,
        ),
        TestCase(
            given=[
                "ZZLéana-V",
                "ZZCloé-V",
                "ZZUò-V",
                "ZZMélia-V",
                "ZZDaphnée-V",
                "ZZMélissandre-V",
                "ZZFèi-V",
                "ZZTáng-V",
            ],
            expected=8,
        ),
        TestCase(
            given=[
                "ZZStéphanie-A",
                "ZZEdmée-K",
                "ZZMaëlla-K",
                "ZZOcéanne-K",
                "ZZGéraldine-K",
                "ZZMaëline-K",
                "ZZNaéva-K",
                "ZZMaëline-K",
                "ZZRuì-K",
                "ZZLéana-V",
                "ZZPublicité-A",
                "ZZCloé-V",
                "ZZUò-V",
                "ZZKù-A",
                "ZZMélia-V",
                "ZZAdélaïde-A",
                "ZZDaphnée-V",
                "ZZÖrjan-A",
                "ZZMélissandre-V",
                "ZZFèi-V",
                "ZZTáng-V",
            ],
            expected=21,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        assert_equals(
            message=f"> guests= {test_case.given}",
            expected=test_case.expected,
            actual=task11(test_case.given),
        )
