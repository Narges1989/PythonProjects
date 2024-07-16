import pytest

from src.py106.guide5 import guide5
from tests.helper.custom_assertions import assert_almost_equals
from tests.helper.TestCase import TestCase


class TestGuide5:
    test_cases = [
        TestCase(given=[4.5, 4.0, 3.5], expected=4.0),
        TestCase(given=[3.0, 3.0, 3.0, 3.0], expected=3.0),
        TestCase(given=[2.0, 5.0, 4.3, 4.2, 4.1], expected=3.92),
        TestCase(given=[3.5, 5.0, 4.3, 4.4, 4.5, 4.7, 3.2], expected=4.2285),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_grading(self, test_case):
        classroom = test_case.given

        assert_almost_equals(
            message=f"> classroom = {classroom}",
            expected=test_case.expected,
            actual=guide5(classroom=classroom),
        )

    def test_failing_scenario(self):
        with pytest.raises(AssertionError):
            guide5(classroom=[])
