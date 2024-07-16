from to_do import TODO


def guide12(a: int, b: int) -> list[int]:
    result = []
    for number in range(a+1,b):
        if number % 2 != 0 and number % 5 == 0:
            result.append(number*3)
        elif  number % 2 == 0 and number % 5 == 0:
            result.append(number*5)
        else:
            result.append(number)
    return result