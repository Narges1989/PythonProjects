from to_do import TODO


def guide16(sentence: str) -> str:
    strEven = ""
    for index in range(len(sentence)):
        if index%2== 0:
            strEven = strEven + sentence[index]
    return strEven

if __name__ == '__main__':
    #sentence=Gothenburg, output = Gtebr
    print(guide16('Gothenburg'))
