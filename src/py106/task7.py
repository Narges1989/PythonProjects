from to_do import TODO


def task7(sentence: str) -> dict[str, int]:
    result = {'letters':0,'digits':0}
    if sentence is None:
        return result
    letters = 0
    digits = 0
    for element in sentence:
        if element.isdigit()== True:
            digits += 1
        elif element.isalpha() == True:
            letters += 1
    result['letters'] = letters
    result['digits'] = digits

    return result


