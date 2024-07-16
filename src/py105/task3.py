from to_do import TODO


def task3(a: dict[int, str], b: dict[int, str]) -> list[int]:
    result = []
    for keyA in a.keys():
        if keyA in b.keys():
            result.append(keyA)

    return result