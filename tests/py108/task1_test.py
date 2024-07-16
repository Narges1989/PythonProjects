from src.py108 import task1
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import assert_almost_equals, assert_class_signature
from tests.helper.FunctionSignature import FunctionSignature


class TestTask1:
    def test_perimeter_of_a_rectangle(self):
        self.__assert_class_signature()

        module = task1
        class_name = "Rectangle"
        base = 65.0
        height = 1.0
        sut = getattr(module, class_name)(base, height)

        assert_almost_equals(
            message=f"Calculate the perimeter of the rectangle with base= {base} and height= {height}",
            expected=132.0,
            actual=sut.perimeter(),
        )

    def test_area_of_a_rectangle(self):
        self.__assert_class_signature()

        module = task1
        class_name = "Rectangle"
        base = 65.0
        height = 1.0
        sut = getattr(module, class_name)(base, height)

        assert_almost_equals(
            message=f"Calculate the area of the rectangle with base= {base} and height= {height}",
            expected=65.0,
            actual=sut.area(),
        )

    def __assert_class_signature(self):
        module = task1
        class_name = "Rectangle"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=["base", "height"],
                methods=[
                    FunctionSignature(
                        function_name="perimeter", number_of_parameters=1
                    ),
                    FunctionSignature(function_name="area", number_of_parameters=1),
                ],
            ),
        )
