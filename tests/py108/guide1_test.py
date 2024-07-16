from src.py108 import guide1
from tests.helper.custom_assertions import *
from tests.helper.FunctionSignature import FunctionSignature


class TestGuide1:
    def test_student_properties_1(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            firstname="Humberto",
            lastname="Linero",
            learner_id=1818,
            department="Engineering",
            major="Computer Science",
        )
        assert_equals(
            message="Asserting firstname", expected="Humberto", actual=learner.firstname
        )
        assert_equals(
            message="Asserting last name", expected="Linero", actual=learner.lastname
        )
        assert_equals(message="Asserting ID", expected=1818, actual=learner.learnerId)
        assert_equals(
            message="Asserting department",
            expected="Engineering",
            actual=learner.department,
        )
        assert_equals(
            message="Asserting major", expected="Computer Science", actual=learner.major
        )

    def test_student_properties_2(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            firstname="John",
            lastname="Jasson",
            learner_id=1978,
            department="Economics",
            major="Accounting",
        )
        assert_equals(
            message="Asserting firstname", expected="John", actual=learner.firstname
        )
        assert_equals(
            message="Asserting last name", expected="Jasson", actual=learner.lastname
        )
        assert_equals(message="Asserting ID", expected=1978, actual=learner.learnerId)
        assert_equals(
            message="Asserting department",
            expected="Economics",
            actual=learner.department,
        )
        assert_equals(
            message="Asserting major", expected="Accounting", actual=learner.major
        )

    def test_details(self, capfd):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner()
        learner.details()
        assert_printed(
            message="-",
            expected="--- Learner Details ---\nName: Learner name\nID: LEARNER ID\nDepartment: LEARNER DEPARTMENT\nMajor: LERNER MAJOR\n",
            pattern="--- Learner Details ---\nName: [a-zA-ZöÖäÄåÅ\\s]*\nID: [0-9]*\nDepartment: [a-zA-ZöÖäÄåÅ\\s]*\nMajor: [a-zA-ZöÖäÄåÅ\\s]*\n",
            capfd=capfd,
        )

    def test_gpa_1(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 1", 4.0, False, ""),
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 3", 5.0, False, ""),
            ]
        )

        assert_almost_equals(
            message="Find the gpa of the student",
            expected=3.6667,
            actual=learner.gpa(),
        )

    def test_gpa_2(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 1", 4.0, False, ""),
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 3", 3.0, False, ""),
                self.course("Class 5", 5.0, False, ""),
            ]
        )

        assert_equals(
            message="Find the gpa of the student",
            expected=3.5,
            actual=learner.gpa(),
        )

    def test_highest_course_1(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 1", 4.0, False, ""),
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 3", 5.0, False, ""),
            ]
        )

        assert_equals(
            message="Find the highest grade of the student",
            expected={"Class 3": 5.0},
            actual=learner.highestCourse(),
        )

    def test_highest_course_2(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 1", 4.0, False, ""),
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 3", 3.0, False, ""),
            ]
        )

        assert_equals(
            message="Find the highest grade of the student",
            expected={"Class 1": 4.0},
            actual=learner.highestCourse(),
        )

    def test_lowest_course_1(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 1", 4.0, False, ""),
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 3", 5.0, False, ""),
            ]
        )

        assert_equals(
            message="Find the highest grade of the student",
            expected={"Class 2": 2.0},
            actual=learner.lowestCourse(),
        )

    def test_lowest_course_2(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 1", 3.0, False, ""),
                self.course("Class 3", 1.0, False, ""),
            ]
        )

        assert_equals(
            message="Find the highest grade of the student",
            expected={"Class 3": 1.0},
            actual=learner.lowestCourse(),
        )

    def test_add_course_1(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 2", 2.0, False, ""),
                self.course("Class 1", 3.0, False, ""),
                self.course("Class 3", 1.0, False, ""),
            ]
        )

        assert_equals(
            message="Provide the grades",
            expected=sorted([2.0, 3.0, 1.0]),
            actual=sorted(learner.grades()),
        )

    def test_add_course_2(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = self.learner(
            courses=[
                self.course("Class 2", 12.0, False, ""),
                self.course("Class 1", 13.0, False, ""),
                self.course("Class 3", 21.0, False, ""),
            ]
        )

        assert_equals(
            message="Provide the grades",
            expected=sorted([12.0, 13.0, 21.0]),
            actual=sorted(learner.grades()),
        )

    def test_school(self):
        self.__assert_Learner_signature()
        self.__assert_Course_signatures()

        learner = getattr(guide1, "Learner")

        assert_equals(message="-", expected="LTH", actual=learner.School)

    def __assert_Course_signatures(self):
        module = guide1
        class_name = "Course"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=["name", "grade", "elective", "department"],
                methods=[],
            ),
        )

    def __assert_Learner_signature(self):
        module = guide1
        class_name = "Learner"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=[
                    "firstname",
                    "lastname",
                    "learner_id",
                    "department",
                    "major",
                ],
                methods=[
                    FunctionSignature(function_name="details", number_of_parameters=1),
                    FunctionSignature(function_name="gpa", number_of_parameters=1),
                    FunctionSignature(
                        function_name="highestCourse", number_of_parameters=1
                    ),
                    FunctionSignature(
                        function_name="lowestCourse", number_of_parameters=1
                    ),
                    FunctionSignature(
                        function_name="addCourse", number_of_parameters=2
                    ),
                    FunctionSignature(function_name="grades", number_of_parameters=1),
                ],
            ),
        )

    def course(self, name, grade, elective, department):
        module = guide1
        class_name = "Course"

        return getattr(module, class_name)(name, grade, elective, department)

    def learner(
        self,
        firstname="",
        lastname="",
        learner_id=18,
        department="",
        major="",
        courses=None,
    ):
        module = guide1
        class_name = "Learner"

        learner = getattr(module, class_name)(
            firstname,
            lastname,
            learner_id,
            department,
            major,
        )

        if courses is not None:
            for course in courses:
                learner.addCourse(course)

        return learner
