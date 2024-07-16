from typing import Callable

from to_do import TODO
from linero_tech_errors import MissingGradesError, LowAttendanceError

def guide3(script: Callable[[], list[float]]) -> float:
    """
    Use the code `from linero_tech_errors import MissingGradesError, LowAttendanceError`
    to import the necessary errors
    """
    max_grade = 0
    try:
        grades = script()
        # for grade in grades:
        #     if grade>max_grade:
        #         max_grade = grade
        return max(grades)
    except MissingGradesError:
        return -1
    except LowAttendanceError:
        return -2