from src.py104.guide18 import guide18
from tests.helper.custom_assertions import assert_equals


class TestGuide18:
    def test_task_grading(self):
        assert_equals(
            message="-",
            expected=(
                "A",
                "b",
                "c",
                "d",
                "E",
                "f",
                "g",
                "h",
                "I",
                "j",
                "k",
                "l",
                "m",
                "n",
                "O",
                "p",
                "q",
                "r",
                "s",
                "t",
                "U",
                "v",
                "w",
                "x",
                "y",
                "z",
            ),
            actual=guide18(),
        )
