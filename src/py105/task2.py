from to_do import TODO


def task2(mapa: dict[int, int]) -> int:
    '''result = 0
    for number in mapa.keys():
        result += number'''
    result = sum(mapa.keys())
    return result