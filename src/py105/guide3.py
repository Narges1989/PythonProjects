from to_do import TODO


def guide3(classroom: dict[str, float], students: list[str]) -> str:
    highest_grade = -1
    highest_student = ''

    for student in students:
        if student in classroom.keys():
            student_grade = classroom[student]
            if student_grade>highest_grade:
                highest_student = student
                highest_grade = student_grade

    return highest_student
if __name__== "__main__":
    print(guide3({"Jane" : 10.0, "John" : 9.5, "Petter" : 8.0},["Petter", "Jose", "Richard", "Ana"]))
