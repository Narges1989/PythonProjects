import string

from to_do import TODO
import string

def guide18() -> tuple[str]:
    vowels = ['a','e','i','o','u']
    # result = []
    # for letter in string.ascii_lowercase:
    #     if letter in vowels:
    #         result.append(letter.upper())
    #     else:
    #         result.append(letter)
    #
    # return tuple(result)

    #return tuple([letter.upper() if letter in vowels else letter for letter in string.ascii_lowercase])


    return tuple(map(lambda letter:letter.upper() if letter in vowels else letter ,string.ascii_lowercase))
