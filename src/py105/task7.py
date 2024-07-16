from to_do import TODO


def task7(words: list[str]) -> dict[int, str]:
    result = {}
    for index, value in enumerate(words):
        result[index] = value
    return result
