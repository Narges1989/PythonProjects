from src.py101.task6 import task6
from tests.helper.custom_assertions import assert_pseudocode


class TestTask6:
    def test_task_grading(self):
        assert_pseudocode(actual=task6())
