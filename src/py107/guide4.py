# TODO("Delete this 'TODO' and create your function here")
def equalizer(word1:str,word2:str) -> list[str]:
    return list(set([letter for letter in word1 if letter in word2]))


if __name__ == '__main__':
    print(equalizer(word1='This is book', word2= 'That is window'))