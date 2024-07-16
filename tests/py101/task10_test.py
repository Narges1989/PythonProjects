from src.py101.task10 import task10
from tests.helper.custom_assertions import assert_pseudocode


class TestTask10:
    def test_task_grading(self):
        assert_pseudocode(actual=task10())
