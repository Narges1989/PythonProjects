from src.py101.guide8 import guide8
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide8:
    def test_task_grading(self):
        assert_pseudocode(actual=guide8())
