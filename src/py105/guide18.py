from to_do import TODO


def guide18(classroom: list[dict[str, float]]) -> float:
    if len(classroom) == 0:
        return 0
    result = 0
    for grade in classroom:
        result += grade['gpa']

    return result/len(classroom)
