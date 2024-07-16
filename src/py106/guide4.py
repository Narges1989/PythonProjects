from typing import Callable
from linero_tech_errors import InvalidAgeError, MissingAgeError
from to_do import TODO


def guide4(script: Callable[[], list[int]]) -> list[int]:
    """
    Use the code `from linero_tech_errors import InvalidAgeError, MissingAgeError`
    to import the necessary errors
    """
    try:
        ages = script()
        return list(filter(lambda age:age>=18,ages))
    except InvalidAgeError:
        return [0,0,0]
    except MissingAgeError:
        return [1, 1, 1]
