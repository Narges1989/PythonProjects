from to_do import TODO


def task2(items: list[int]) -> int:
    if items is None:
        return 0
    result = 0
    for item in items:
        if item == None:
            result += 1

    return result
