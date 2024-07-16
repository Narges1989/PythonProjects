from to_do import TODO
import re
from datetime import datetime


def task9(identification: str) -> bool:
    if identification is None or len(identification)<13:
        return False
    date = re.split('-',identification)
    if not(date[0].isdigit()) or not(date[1].isdigit()):
        return False
    print(date[0][0:4])
    format = '%Y%m%d'
    result = False
    if int((date[0][0:4])) > 1946:
        try:
            result = bool(datetime.strptime(date[0],format))
        except ValueError:
            result = False

    return result

if __name__ == "__main__":
    print(task9('19470430-3669'))
