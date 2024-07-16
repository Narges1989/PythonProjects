from to_do import TODO


def task8(sentence: str, character: str) -> int:
    result = sentence.count(character)
    return result

if __name__ == '__main__':
    # I code in KOTLIN, output = 2
    print(task8('I code in KOTLIN','I'))

    # 'Gooood Bype GBG', output = 4
    print(task8('Gooood Bype GBG','o'))

