from to_do import TODO


def guide2(items: list[int]) -> int:
    if len(items)!=3:
        return -1
    max = items[0]
    if items[1]>items[0]:
        max = items[1]
    if items[2]>items[1]:
        max = items[2]
    return max
