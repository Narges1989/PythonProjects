from to_do import TODO


def guide10(items: list[str]) -> list[str]:
    #solution 3
    transformed_list = map(
        lambda index_element:index_element[1].upper() if index_element[0] % 2 == 0 else index_element[1].lower(),
        enumerate(items))
    return transformed_list

""" result = []
    for index,word in enumerate(items):
        if index % 2 == 0:
            result.append(word.upper())
        else:
            result.append(word.lower())
    return result"""
    # solution 2
    # return [item.upper() if index % 2 == 0 else item.lower() for index,item in enumerate(items)]
