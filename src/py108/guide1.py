import math
class Course:
    def __init__(self,name, grade, elective, department):
        self.name = name
        self.grade = grade
        self.elective = elective
        self.department = department



class Learner:
    School = 'LTH'
    def __init__(self, firstname, lastname, learner_id, department, major):
        self.firstname = firstname
        self.lastname = lastname
        self.learnerId = learner_id
        self.department = department
        self.major = major
        self.__courses = []

    def details(self):
        print('--- Learner Details ---')
        print(f'Name: {self.firstname} {self.lastname}')
        print(f'ID: {self.learnerId}')
        print(f'Department: {self.department}')
        print(f'Major: {self.major}')

    def gpa(self):
        if len(self.__courses) == 0:
            return 0
        result = 0
        for course in self.__courses:
            result += course.grade
        return result/ len(self.__courses)

    def highestCourse(self):
        course_max = ''
        grade_max = 0

        for course in self.__courses:
            if course.grade > grade_max:
                grade_max = course.grade
                course_max = course.name

        return {course_max:grade_max}

    def lowestCourse(self):
        course_min = ''
        grade_min = 10000
        result = {}
        for course in self.__courses:
            if course.grade < grade_min:
                grade_min = course.grade
                course_min = course.name

        return {course_min: grade_min}

    def addCourse(self,course: Course):
        self.__courses.append(course)

    def grades(self):
        grades = []
        for course in self.__courses:
            grades.append(course.grade)

        return grades

if __name__== "__main__":
    student1 = Learner('John','Smith', 1818,'Engineering', 'Computer Engineering' )
    student1.details()

    programming = Course('C++',5,True,'Engineering')
    math = Course('math', 3.5, True, 'Engineering')
    course1= Course("Class 1", 4.0, False, "")
    course2 =  Course("Class 2", 2.0, False, "")
    course3 = Course("Class 2", 2.0, False, "")
    student1.addCourse(course1)
    student1.addCourse(course2)
    student1.addCourse(course3)

    print(student1.highestCourse())
    print(student1.lowestCourse())


    print(student1.grades())