from src.py101.guide1 import guide1
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide1:
    def test_task_grading(self):
        assert_pseudocode(actual=guide1())
