from to_do import TODO


def guide5(a: float, b: float, c: float) -> float:
    result = a + b + c
    return result

if __name__ == '__main__':
    # a = 5, b = 15, c = 11 -> 31
    print(guide5(5,15,11))

    # a = 7.0, b = 5.0, c = 5.0 -> 114
    print(guide5(7.0,5.0,5.0))
