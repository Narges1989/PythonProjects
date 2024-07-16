from src.py105.task1 import task1
from tests.helper.custom_assertions import assert_equals


class TestTask1:
    def test_task_grading(self):
        assert_equals(
            message="-",
            expected={10: 20, 12: 24, 14: 28, 16: 32, 18: 36, 20: 40},
            actual=task1(),
        )
