from to_do import TODO


def task5(items: list[int]) -> list[int]:
    # result = []
    # for index,number in enumerate(items):
    #     result.append(index*number)
    # return result

    return [index*number for index,number in enumerate(items)]
