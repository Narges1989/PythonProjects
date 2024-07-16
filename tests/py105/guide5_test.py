import pytest

from src.py105.guide5 import guide5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestGuide5:
    test_cases = [
        TestCase(given={}, expected={}),
        TestCase(
            given={"UTP": "Panama", "KTH": "Sweden", "MIT": "USA"},
            expected={"Panama": "UTP", "Sweden": "KTH", "USA": "MIT"},
        ),
        TestCase(
            given={
                "USMA": "Panama",
                "UNITO": "Italy",
                "Chalmers": "Sweden",
                "USF": "USA",
            },
            expected={
                "Panama": "USMA",
                "Italy": "UNITO",
                "Sweden": "Chalmers",
                "USA": "USF",
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        universities = test_case.given

        assert_equals(
            message=f"> universities = {universities}",
            expected=test_case.expected,
            actual=guide5(universities),
        )
