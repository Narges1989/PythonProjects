from to_do import TODO


def task2(items: list[int]) -> int:
    if items == []:
        return 0
    result = 0
    for index,number in enumerate(items):
        if index %2 == 0:
            result += number
    return result

