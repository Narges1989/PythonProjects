from src.py103.task4 import task4
from tests.helper.custom_assertions import assert_equals


class TestTask4:
    def test_task_grading(self):
        assert_equals(
            message="-",
            expected=55944,
            actual=task4(),
        )
