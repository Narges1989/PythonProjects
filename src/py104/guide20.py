from to_do import TODO


def guide20(a: set[int], b: set[int]) -> set[int]:
    # result = set()
    # for item in a:
    #     if item in b:
    #         result.add(item)
    # return result
    return set((item for item in a if item in b))
