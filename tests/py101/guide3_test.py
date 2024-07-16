from src.py101.guide3 import guide3
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide3:
    def test_task_grading(self):
        assert_pseudocode(actual=guide3())
