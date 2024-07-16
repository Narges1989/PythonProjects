from to_do import TODO


def task6(mapa: dict[int, str], parameter: str) -> dict[int, str]:
    '''result = {}
    for key,value in mapa.items():
        if value == parameter:
            result[key] = value

    return result'''

    return {key:value for key,value in mapa.items() if value == parameter}