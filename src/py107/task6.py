# TODO("Delete this 'TODO' and create your function here")
import string
def counter(word:str) -> bool:
    sum = 0
    for letter in word.replace(' ',''):
        sum += string.ascii_lowercase.index(letter.lower()) + 1

    return sum & 1 == 0
print(counter('AlExa MauRi')