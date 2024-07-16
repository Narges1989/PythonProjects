from src.py101.task9 import task9
from tests.helper.custom_assertions import assert_pseudocode


class TestTask9:
    def test_task_grading(self):
        assert_pseudocode(actual=task9())
