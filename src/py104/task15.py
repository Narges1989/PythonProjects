from to_do import TODO


def task15(sells: list[int]) -> int:
    result = 0
    for sell in sells:
        result += sell
    return result
