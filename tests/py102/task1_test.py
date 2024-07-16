from src.py102.task1 import task1
from tests.helper.custom_assertions import assert_printed


class TestTask1:
    def test_task_is_implemented(self, capfd):
        task1()
        assert_printed(
            message="-",
            expected="Country: COUNTRY NAME\nCapital: CAPITAL NAME\nCurrency: CURRENCY NAME\n",
            pattern="Country: [a-zA-ZöÖäÄåÅ\\s]*\nCapital: [a-zA-ZöÖäÄåÅ\\s]*\nCurrency: [a-zA-Z\\s]*\n",
            capfd=capfd,
        )
