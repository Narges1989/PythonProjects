from to_do import TODO


def task10(mapa: dict[int, str]) -> dict[str, int]:
    '''result = {}
    for key, value in mapa.items():
        result[value] = key
    return result'''

    return {value:key for key, value in mapa.items()}