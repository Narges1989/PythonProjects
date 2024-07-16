from to_do import TODO


def task10(items: list[str]) -> int:

    # if 'Nemo' in items:
    #     result = items.index('Nemo')
    # else:
    #     result = None
    # return items.index('Nemo') if 'Nemo' in items else None
    #
    if 'Nemo' not in items:
        result = None
    for index,item in enumerate(items):
        if item == 'Nemo':
            result = index
            break
    return result

