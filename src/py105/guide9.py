from to_do import TODO


def guide9(word: str) -> dict[str, int]:
    # result = {}
    # for letter in word:
    #     if letter not in result.keys():
    #         number_of_letters = word.count(letter)
    #         result[letter] = number_of_letters
    # return result

    # solution 2
    result = {}
    for letter in word:
        result[letter] = result.get(letter,0) + 1

    return result

