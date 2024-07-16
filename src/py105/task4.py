from to_do import TODO


def task4(mapa: dict[int, int], parameter: int) -> list[int]:
    '''result = []

    for key,value in mapa.items():
        if value == parameter:
            result.append(key)

    return result'''
    return [key for key,value in mapa.items() if value == parameter]
