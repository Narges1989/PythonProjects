from to_do import TODO


def guide10(names: list[str]) -> dict[str, int]:
    # result = {}
    # for name in names:
    #     result[name] = result.get(name,0)+1
    # return result

    # solution 2
    # result = {}
    # for name in names:
    #     if name not in result.keys():
    #         result[name] = names.count(name)
    # return result

    #solution 3
    result = {}
    result = {name:names.count(name) for name in names if name not in result}
    return result