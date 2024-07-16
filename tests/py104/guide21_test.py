import pytest

from src.py104.guide21 import guide21
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide21:
    test_cases = [
        # given1 is a and given2 is b
        TestCase2(
            given1={"jim@gmail.com", "jane@outlook.se", "info@alpha.se"},
            given2={"jim@gmail.com", "jane@outlook.se", "info@beta.se", "info@vcs.se"},
            expected={"info@beta.se", "info@vcs.se"},
        ),
        TestCase2(
            given1={
                "hola@info-co.com",
                "lola@lidna.se",
                "lunar@lenki.org",
                "tor@tar.com",
            },
            given2={"nathan@gmail.com", "nod@outlook.se", "todd@programming.se"},
            expected={"nathan@gmail.com", "nod@outlook.se", "todd@programming.se"},
        ),
        TestCase2(
            given1={
                "Jolene_Nichol@mpibr.co",
                "Catherine@voylg.catering",
                "Bryon@yfxpw.sol",
                "Carol_Asher@dbxli.org",
            },
            given2={
                "Jolene_Nichol@mpibr.co",
                "Catherine@voylg.catering",
                "Bryon@yfxpw.sol",
                "Carol_Asher@dbxli.org",
            },
            expected=set(),
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        a = test_case.given1
        b = test_case.given2

        assert_equals(
            message=f"> a = {a}\n> b = {b}",
            expected=test_case.expected,
            actual=guide21(a=a, b=b),
        )
