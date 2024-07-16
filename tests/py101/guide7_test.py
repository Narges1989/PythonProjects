from src.py101.guide7 import guide7
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide7:
    def test_task_grading(self):
        assert_pseudocode(actual=guide7())
