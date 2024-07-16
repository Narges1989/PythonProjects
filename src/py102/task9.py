from to_do import TODO


def task9(sentence: str, character: str) -> bool:
    if (character.lower() in sentence) or (character.upper() in sentence):
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    # I code in KOTLIN, output = True
    print(task9('I code in KOTLIN','i'))

    # 'Stockholm', output = False
    print(task9('Stockholm','n'))