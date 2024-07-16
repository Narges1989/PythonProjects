from to_do import TODO


def guide4(a: int, b: int) -> list[int]:
    result = []
    if a>=b:
        return result
    for item in range(a,b+1):
        if item % 2 != 0 and item%5 == 0:
            result.append(pow(item,2))
        elif item % 2 != 0:
            result.append(item)
    return result
