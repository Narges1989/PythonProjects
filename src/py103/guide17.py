from to_do import TODO


def guide17(sentence: str) -> str:
    i = 0
    result = ''
    for index, letter in enumerate(sentence):
        if index%2 == 0:
            result = result + letter.upper()
        else:
            result = result + letter.lower()
    return result

if __name__ == '__main__':
    #sentence=Gothenburg, output = GoThEnBeRg
    print(guide17('Gothenburg'))
