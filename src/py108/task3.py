# TODO("Delete this 'TODO' and create your class here")
class Student:
    def __init__(self,grades:list[float]):
        self._grades = grades

    @property
    def grades(self):
        print("Getting value...")
        return self._grades
    def gpa(self) -> float:
        if len(self._grades == 0):
            return 0.0
        return sum(self._grades)/len(self._grades)

    def bonus(self):
        self._grades = [grade + 1 for grade in self._grades]

    def lowest(self) -> float:
        return min(self._grades)


    def highest(self) -> float:
        return max(self._grades)

if __name__ == '__main__':
    std = Student([4,3.5,2.2,4.7,1.3])
    print(std.gpa())
    std.bonus()
    print(std.lowest())
    print(std.highest())

    print(std.grades)