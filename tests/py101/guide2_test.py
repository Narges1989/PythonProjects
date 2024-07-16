from src.py101.guide2 import guide2
from tests.helper.custom_assertions import assert_pseudocode


class TestGuide2:
    def test_task_grading(self):
        assert_pseudocode(actual=guide2())
