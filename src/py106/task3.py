from to_do import TODO


def task3(sentence: str) -> str:
    vowels = ['a','e','i','o','u']

    if sentence is None or len(sentence) == 0:
        return '*'

    result = ''
    for letter in sentence:
        if letter.lower() in vowels:
            result += '*'
        else:
            result += letter

    return result

