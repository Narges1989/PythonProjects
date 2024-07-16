from to_do import TODO


def guide2(month: str) -> bool:
    if ((month.lower()) == 'november'):
        return True
    else:
        return False

if __name__== "__main__":
    # November, november, NOVEMBER , output = True
    print(guide2('NovembeR'))

    # MArch,march , output = False
    print(guide2('MArch'))

