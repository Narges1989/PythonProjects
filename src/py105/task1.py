from to_do import TODO


def task1() -> dict[int, int]:
    result = {}
    for number in range(10, 21):
        if number%2 == 0:
            result[number] = number*2
    return result