from to_do import TODO


def guide19(a: int, b: int) -> tuple[int]:
    # result = []
    # for number in range(a,b+1):
    #     if number%2 != 0 and number % 3 == 0:
    #         result.append(number)
    # return tuple(result)

    return tuple(number for number in range(a,b+1) if number%2 != 0 and number % 3 == 0)
