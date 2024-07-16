from to_do import TODO


def task8(items: list[str]) -> list[str]:
    # result = []
    #
    # for item in items:
    #     if item is not None and len(item)>3:
    #         result.append(item)
    #
    # return result
    #return [item for item in items if item is not None and len(item)>3]

    return list(filter(lambda item:item is not None and len(item)>3,items))