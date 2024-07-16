from src.py108 import task5
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import assert_almost_equals, assert_class_signature
from tests.helper.FunctionSignature import FunctionSignature


class TestTask5:
    def test_perimeter_of_a_circle(self):
        self.__assert_class_signature()

        module = task5
        class_name = "Circle"
        radius = 65.3
        sut = getattr(module, class_name)(radius)

        assert_almost_equals(
            message=f"Implement a function which returns the perimeter of a circle.\n> radius= {radius}",
            expected=410.29,
            actual=sut.perimeter(),
        )

    def test_area_of_a_circle(self):
        self.__assert_class_signature()

        module = task5
        class_name = "Circle"
        radius = 50.1
        sut = getattr(module, class_name)(radius)

        assert_almost_equals(
            message=f"Implement a function which returns the area of a circle.\n> radius= {radius}",
            expected=7885.43,
            actual=sut.area(),
        )

    def __assert_class_signature(self):
        module = task5
        class_name = "Circle"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=["radius"],
                methods=[
                    FunctionSignature(function_name="area", number_of_parameters=1),
                    FunctionSignature(
                        function_name="perimeter", number_of_parameters=1
                    ),
                ],
            ),
        )
