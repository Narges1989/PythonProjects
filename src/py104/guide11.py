from to_do import TODO


def guide11(items: list[int]) -> list[int]:
    # solution 3
    transfered_list = map(
        lambda number: number*3 if number % 11 == 0 else number,
        items)
    return transfered_list
    # solution 2
   # return [number * 3 if number % 11 == 0 else number for number in items]
"""    result = []
    for number in items:
        if number % 11 == 0:
            result.append(number*3)
        else:
            result.append(number)
    return result"""

