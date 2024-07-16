from to_do import TODO


def task3(items: list[int]) -> list[int]:
    result = []
    for number in items:
        if items.count(number)>1 and number not in result:
            result.append(number)
    return result
