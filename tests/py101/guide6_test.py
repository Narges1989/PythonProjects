from src.py101.guide6 import guide6
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide6:
    def test_task_grading(self):
        assert_pseudocode(actual=guide6())
