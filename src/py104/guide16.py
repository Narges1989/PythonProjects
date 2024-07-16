from to_do import TODO


def guide16(items: tuple[str]) -> list[str]:
    # result = []
    # for item in items:
    #     if item[0] == 'H' or item[0] == 'h':
    #         result.append(item)
    # return result

    #return [item for item in items if item[0] == 'H' or item[0] == 'h']
    return list(filter(lambda item: item[0] == 'H' or item[0] == 'h' ,items))
