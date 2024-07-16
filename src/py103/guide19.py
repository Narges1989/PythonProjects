from to_do import TODO


def guide19(sentence: str) -> str:
    reverse_sent = ''
    index = len(sentence) - 1
    while index>= 0:
        reverse_sent += sentence[index]
        index -= 1
    return reverse_sent

if __name__ == '__main__':
    #sentence=ABCD, output = DCBA
    print(guide19('ABCD'))
