from src.py101.task4 import task4
from tests.helper.custom_assertions import assert_pseudocode


class TestTask4:
    def test_task_grading(self):
        assert_pseudocode(actual=task4())
