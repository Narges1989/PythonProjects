# TODO("Delete this 'TODO' and create your class here")
class Rectangle:
    def __init__(self,base: float ,height: float):
        self.__base = base
        self.__height = height
    def perimeter(self):
        return ((self.__base+self.__height) *2)

    def area(self):
        return (self.__base*self.__height)