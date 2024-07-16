from src.py101.guide4 import guide4
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide4:
    def test_task_grading(self):
        assert_pseudocode(actual=guide4())
