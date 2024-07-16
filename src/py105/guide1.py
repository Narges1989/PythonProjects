from to_do import TODO


def guide1(a: int, b: int) -> dict[int, int]:
    # result = dict({})
    #
    if a>=b:
        return {}
    # # solution 1: with For loop
    # for key in range(a,b+1):
    #     if key %2 == 0:
    #         result[key] = 2*key
    #     else:
    #         result[key] = 3*key
    #
    # # solution 2: refactoring
    # result = {}
    # for key in range(a, b + 1):
    #     result[key] = 2*key if key %2 == 0 else 3*key
    # return result
    #
    # solution 3: dictionary comprehension
    return {key:2*key if key %2 == 0 else key*3 for key in range(a, b + 1)}


