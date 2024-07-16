from to_do import TODO


def guide20(sentence: str, character: str) -> int:
    index = 0
    while index<len(sentence):
        if character.lower()== sentence[index].lower():
            return index
            break
        index = index + 1

if __name__ == '__main__':
    #sentence=Gothenburg,character = 'o', output = 1
    print(guide20('Gothenburg','o'))




