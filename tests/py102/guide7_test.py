import pytest

from src.py102.guide7 import guide7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase2


class TestGuide7:
    test_cases = [
        # given1 is country and given2 is capital
        TestCase2(
            given1="Panamá",
            given2="Ciudad de Panamá",
            expected="The capital of Panamá is Ciudad de Panamá",
        ),
        TestCase2(
            given1="Sweden",
            given2="Stockholm",
            expected="The capital of Sweden is Stockholm",
        ),
        TestCase2(
            given1="Costa Rica",
            given2="San José",
            expected="The capital of Costa Rica is San José",
        ),
        TestCase2(
            given1="Colombia",
            given2="Bogotá",
            expected="The capital of Colombia is Bogotá",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        country = test_case.given1
        capital = test_case.given2

        assert_equals(
            message=f"> country = {country}\n> capital = {capital}",
            expected=test_case.expected,
            actual=guide7(country=country, capital=capital),
        )
