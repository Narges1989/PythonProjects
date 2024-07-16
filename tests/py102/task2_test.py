from src.py102.task2 import task2
from tests.helper.custom_assertions import assert_printed


class TestTask2:
    def test_task_is_implemented(self, capfd):
        task2()
        assert_printed(
            message="-",
            expected="Hello <NAME>, you are from <COUNTRY> and you were born in <MONTH_OF_BIRTH>",
            pattern="Hello [a-zA-ZöÖäÄåÅ\\s]*, you are from [a-zA-ZöÖäÄåÅ\\s]* and you were born in [a-zA-Z\\s]*",
            capfd=capfd,
        )
