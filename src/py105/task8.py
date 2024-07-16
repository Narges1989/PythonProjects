from to_do import TODO


def task8(grades: dict[str, list[float]]) -> str:
    Max_avg = 0
    for key,value in grades.items():
        avg = sum(value)/len(value)
        if avg > Max_avg:
            Max_avg = avg
            result = key
    return result
