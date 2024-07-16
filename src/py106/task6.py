from to_do import TODO


def task6(items: list[int]) -> list[int]:
    if len(items) == 0:
        return []

    result = []
    for index, element in enumerate(items):
        if element is None:
            result.append(None)
        else:
            result.append(index*element)

    return result
