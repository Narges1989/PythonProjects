from to_do import TODO


def task4(sentence: str) -> dict[str, int]:

    if sentence is None or len(sentence) == 0:
        return {}

    result= {'a':0, 'e':0 ,'i':0,'o':0,'u':0}
    vowels = result.keys()

    sentence_lower = sentence.lower()

    for letter in sentence_lower:
        if letter in vowels:
            result[letter] = sentence_lower.count(letter)
    return result

if __name__ == "__main__":
    print(task4('Hello'))



