from src.py108 import task3
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import (
    assert_almost_equals,
    assert_class_signature,
    assert_equals,
)
from tests.helper.FunctionSignature import FunctionSignature


class TestTask3:
    def test_calculates_the_GPA_of_the_students(self):
        self.__assert_class_signature()

        module = task3
        class_name = "Student"
        grades = [77.0, 79.0, 88.0, 90.0, 100.0]
        sut = getattr(module, class_name)(grades)

        assert_almost_equals(
            message=f"Calculate the GPA of the student.\n> grades= {grades}",
            expected=86.8,
            actual=sut.gpa(),
        )

    def test_calculates_the_new_grades_after_adding_a_bonus(self):
        self.__assert_class_signature()

        module = task3
        class_name = "Student"
        grades = [77.0, 79.0, 88.0, 90.0, 100.0]
        sut = getattr(module, class_name)(grades)

        sut.bonus()

        assert_equals(
            message=f"Add 1 bonus point to the grades.\n> grades= {grades}",
            expected=sorted([78.0, 80.0, 89.0, 91.0, 101.0]),
            actual=sorted(sut.grades),
        )

    def test_the_highest_grade_is_returned(self):
        self.__assert_class_signature()

        module = task3
        class_name = "Student"
        grades = [77.0, 79.0, 88.0, 90.0, 100.0]
        sut = getattr(module, class_name)(grades)

        assert_equals(
            message=f"Determine the highest grade.\n> grades= {grades}",
            expected=100.0,
            actual=sut.highest(),
        )

    def test_the_lowest_grade_is_returned(self):
        self.__assert_class_signature()

        module = task3
        class_name = "Student"
        grades = [77.0, 79.0, 88.0, 90.0, 100.0]
        sut = getattr(module, class_name)(grades)

        assert_equals(
            message=f"Determine the lowest grade.\n> grades= {grades}",
            expected=77.0,
            actual=sut.lowest(),
        )

    def __assert_class_signature(self):
        module = task3
        class_name = "Student"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=["grades"],
                methods=[
                    FunctionSignature(function_name="gpa", number_of_parameters=1),
                    FunctionSignature(function_name="bonus", number_of_parameters=1),
                    FunctionSignature(function_name="lowest", number_of_parameters=1),
                    FunctionSignature(function_name="highest", number_of_parameters=1),
                ],
            ),
        )
