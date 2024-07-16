from to_do import TODO


def task7(sentence: str) -> int:
    result = len(sentence)
    return result

if __name__ == '__main__':
    # I love GBG, output = 10
    print(task7('I love GBG'))

    # Good Bype GBG, output = 13
    print(task7('Good Bype GBG'))