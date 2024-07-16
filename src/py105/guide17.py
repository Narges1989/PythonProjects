from to_do import TODO


def guide17(education: dict[str, dict[str, int]]) -> str:
    result = []
    max_enrolled = 0
    for course,value in education.items():
        temp = value['enrolled']
        if temp>max_enrolled:
            max_enrolled = temp
            result = course

    return result
