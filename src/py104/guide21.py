from to_do import TODO


def guide21(a: set[str], b: set[str]) -> set[str]:
    # result = set()
    # for item in b:
    #     if item not in a:
    #         result.add(item)
    #
    # return result

    return set((item for item in b if item not in a))