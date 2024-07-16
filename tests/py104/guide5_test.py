from src.py104.guide5 import guide5
from tests.helper.custom_assertions import assert_equals


class TestGuide5:
    def test_task_grading(self):
        assert_equals(
            message="-",
            expected=[
                "A",
                "b",
                "C",
                "d",
                "E",
                "f",
                "G",
                "h",
                "I",
                "j",
                "K",
                "l",
                "M",
                "n",
                "O",
                "p",
                "Q",
                "r",
                "S",
                "t",
                "U",
                "v",
                "W",
                "x",
                "Y",
                "z",
            ],
            actual=guide5(),
        )
