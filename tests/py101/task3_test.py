from src.py101.task3 import task3
from tests.helper.custom_assertions import assert_pseudocode


class TestTask3:
    def test_task_grading(self):
        assert_pseudocode(actual=task3())
