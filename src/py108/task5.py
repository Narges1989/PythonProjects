# TODO("Delete this 'TODO' and create your class here")
import math
class Circle:
    def __init__(self, radius:float):
        self.__radius = radius

    def area(self)-> float:
        return math.pi * (self.__radius * self.__radius)


    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius