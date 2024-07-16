# TODO("Delete this 'TODO' and create your function here")
# method 1
def remover(sentence: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for letter in sentence:
        if letter.lower() not in vowels:
            result += letter
    return result

print(remover("Sweden is nice"))

