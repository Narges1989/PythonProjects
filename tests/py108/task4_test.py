from src.py108 import task4
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import assert_class_signature, assert_equals
from tests.helper.FunctionSignature import FunctionSignature


class TestTask4:
    def test_the_health_of_the_superhero_reduces_by_one_after_the_hero_is_sick(self):
        self.__assert_class_signature()

        module = task4
        class_name = "Hero"
        sut = getattr(module, class_name)()

        sut.sick()

        assert_equals(
            message="Implement a method called 'sick()' which reduces the health of the superhero by 1.",
            expected=9,
            actual=sut.health,
        )

    def test_the_health_of_the_superhero_increases_by_one_after_a_heal(self):
        self.__assert_class_signature()

        module = task4
        class_name = "Hero"
        sut = getattr(module, class_name)()

        sut.heal()

        assert_equals(
            message="Implement a method called 'heal()' which increases the health of the hero by 1",
            expected=11,
            actual=sut.health,
        )

    def test_the_level_of_the_superhero_increases_by_one_after_the_hero_attacks(self):
        self.__assert_class_signature()

        module = task4
        class_name = "Hero"
        sut = getattr(module, class_name)()

        sut.attack()

        assert_equals(
            message="Implement a method called 'attack()' which increases the level of the hero by one",
            expected=1,
            actual=sut.level,
        )

    def __assert_class_signature(self):
        module = task4
        class_name = "Hero"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=[],
                methods=[
                    FunctionSignature(function_name="sick", number_of_parameters=1),
                    FunctionSignature(function_name="heal", number_of_parameters=1),
                    FunctionSignature(function_name="attack", number_of_parameters=1),
                ],
            ),
        )
