from to_do import TODO


def task1(sentence: str) -> int:
    if sentence is None:
        return 0

    return len(sentence)