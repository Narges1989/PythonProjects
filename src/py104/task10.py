from to_do import TODO


def task10(items: list[int]) -> list[int]:
    # result = []
    # for number in items:
    #     if number % 2 == 0:
    #         result.append(number*2)
    #     else:
    #         result.append(number*3)
    # return result

    return [number*2 if number % 2 == 0 else number*3 for number in items]