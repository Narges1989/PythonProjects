from src.py101.task7 import task7
from tests.helper.custom_assertions import assert_pseudocode


class TestTask7:
    def test_task_grading(self):
        assert_pseudocode(actual=task7())
