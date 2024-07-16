import string

from to_do import TODO
import string

def guide5() -> list[str]:
    alphabet_str = string.ascii_lowercase
    result = []
    for index,letter in enumerate(alphabet_str):
        value_append = letter.upper() if index % 2 == 0 else letter
        result.append(value_append)
    return result


if __name__== "__main__":
    print(guide5())