from to_do import TODO


def guide6(items: list[int]) -> list[int]:
    """result = []
    for item in items:
        if item % 5 == 0 and item>10:
            result.append(item)
    return result"""
    return [item for item in items if item % 5 == 0 and item>10]