from to_do import TODO


def task6(sentence: str) -> str:
    if sentence == '':
        return ''
    # result = ''
    # for index,word in enumerate(sentence):
    #     print(word)
    #     if index % 2 == 0:
    #         result += word.upper()
    #     else:
    #         result += word
    # return result

    # solution 2: list comprehension
    result_out = [word.upper() if index % 2 == 0 else word for index,word in enumerate(sentence)]
    return "".join(result_out)
