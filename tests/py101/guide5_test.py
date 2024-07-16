from src.py101.guide5 import guide5
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide5:
    def test_task_grading(self):
        assert_pseudocode(actual=guide5())
