from src.py101.task8 import task8
from tests.helper.custom_assertions import assert_pseudocode


class TestTask8:
    def test_task_grading(self):
        assert_pseudocode(actual=task8())
