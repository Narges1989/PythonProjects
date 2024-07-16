from to_do import TODO


def guide9(items: list[int]) -> list[int]:
    return [item for item in items if item % 10 == 0]