from to_do import TODO


def task5(word: str) -> bool:
    if word is None or word == '':
        return False

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter)!= 1:
            return False
        else:
            continue
    return True

if __name__ == "__main__":
    print(task5('SwedEn'))

