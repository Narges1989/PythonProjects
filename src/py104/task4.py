from to_do import TODO


def task4(items: list[int], factor: int) -> list[int]:
    result = []
    for number in items:
        if number % factor == 0 and number not in result:
            result.append(number)
    return result
