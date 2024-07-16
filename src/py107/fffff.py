# TODO("Delete this 'TODO' and create your function here")
import string
def censorship(sentence:str) -> str:
    result= []
    text = sentence.split()
    for word in text:
        if word[-1] in string.punctuation:
            word1 = word[:-1]
            if len(word1) > 4:
                star_word = '*' * len(word1) + word[-1]
                result.append(star_word)
