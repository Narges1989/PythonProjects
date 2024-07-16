import pytest

from src.py105.guide2 import guide2
from tests.helper.custom_assertions import assert_equals


class TestGuide2:
    def test_task_grading(self):
        assert_equals(
            message="-",
            expected={
                "a": "A",
                "b": "bb",
                "c": "C",
                "d": "dd",
                "e": "E",
                "f": "ff",
                "g": "G",
                "h": "hh",
                "i": "I",
                "j": "jj",
                "k": "K",
                "l": "ll",
                "m": "M",
                "n": "nn",
                "o": "O",
                "p": "pp",
                "q": "Q",
                "r": "rr",
                "s": "S",
                "t": "tt",
                "u": "U",
                "v": "vv",
                "w": "W",
                "x": "xx",
                "y": "Y",
                "z": "zz",
            },
            actual=guide2(),
        )
