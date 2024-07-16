from src.py101.task2 import task2
from tests.helper.custom_assertions import assert_pseudocode


class TestTask2:
    def test_task_grading(self):
        assert_pseudocode(actual=task2())
