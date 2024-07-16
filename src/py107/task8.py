def vowels(sentence: str) -> int:
    vowels_value = {'a':5, 'e':4, 'i':3, 'o':2, 'u':1}
    result = 0

    for letter in sentence:
        if letter.lower() in vowels_value:
            result += vowels_value[letter.lower()]
    return result

print(vowels('U'))