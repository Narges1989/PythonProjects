from to_do import TODO


def task9(items: list[int]) -> list[int]:
    if len(items) == 0:
        return []
    # result = []
    # for index,number in enumerate(items):
    #     if index == 0:
    #         result.append(number*number)
    #     else:
    #         result.append(number*items[index-1])
    # return result

    return [number*number if index == 0 else number*items[index-1] for index,number in enumerate(items)]
