from typing import Any

from to_do import TODO


def guide9(classroom: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    for student_name,details in classroom.items():
        student_grades = details['grades']
        new_grades = list(map(lambda grade: 0.0 if grade is None else grade,student_grades))
        classroom[student_name]['grades'] = new_grades

    return classroom




