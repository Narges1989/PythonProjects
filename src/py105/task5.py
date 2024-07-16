from to_do import TODO


def task5(mapa: dict[int, int], constant: int) -> list[int]:
    # result = []
    #
    # for key,value in mapa.items():
    #     if value != constant:
    #         result.append(key)
    #
    # return result

    return [key for key,value in mapa.items() if value != constant]
