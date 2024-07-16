from to_do import TODO
import string

def guide2() -> dict[str, str]:
    alphebet = string.ascii_lowercase
    result ={}

    # solution 1: using for loop
    # for index, letter in enumerate(alphebet):
    #     if index % 2 == 0:
    #         result[letter] = letter.upper()
    #     else:
    #         result[letter] = letter + letter
    #
    # return result

    # solution 2: using for ternary operation
    for index, letter in enumerate(alphebet):
        result[letter] = letter.upper() if index % 2 == 0 else letter + letter
    return result


    # solution 3: using dictionary comprehension
    #return {letter:letter.upper() if index % 2 == 0 else letter+letter for index, letter in enumerate(alphebet)}
