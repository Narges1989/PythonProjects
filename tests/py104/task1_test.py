from src.py104.task1 import task1
from tests.helper.custom_assertions import assert_equals


class TestTask1:
    def test_a_random_element_from_the_list_is_selected(self):
        items = ["Panama", "Sweden", "USA", "Spain", "Norway", "Austria", "Portugal"]
        assert_equals(
            message=f"> items: {items}",
            expected=True,
            actual=task1(items) in items,
        )

    def test_a_random_element_from_an_empty_list(
        self,
    ):
        items = []
        assert_equals(
            message=f"> items= {items}",
            expected="",
            actual=task1(items),
        )
