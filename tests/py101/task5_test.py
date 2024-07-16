from src.py101.task5 import task5
from tests.helper.custom_assertions import assert_pseudocode


class TestTask5:
    def test_task_grading(self):
        assert_pseudocode(actual=task5())
