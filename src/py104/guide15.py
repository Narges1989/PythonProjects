from to_do import TODO


def guide15(items: tuple[str]) -> bool:
    # middle_index = int(len(items)/2)
    # if len(items[-1]) == len(items[middle_index]):
    #     return True
    # else:
    #     return False

    result = True if len(items[-1]) == len(items[int(len(items)/2)]) else False
    return result
