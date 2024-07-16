from to_do import TODO


def task7(items: list[int]) -> int:
    if items == []:
        return 0
    Min = items[0]
    for number in items:
        if number<Min:
            Min = number
    return Min

