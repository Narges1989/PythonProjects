from to_do import TODO


def guide12(number: int) -> bool:
    return not number%2


if __name__ == '__main__':
    #input=17, output = False
    print(guide12(17))

    #input=30, output = True
    print(guide12(30))