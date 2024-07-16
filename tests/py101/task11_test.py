from src.py101.task11 import task11
from tests.helper.custom_assertions import assert_pseudocode


class TestTask11:
    def test_task_grading(self):
        assert_pseudocode(actual=task11())
