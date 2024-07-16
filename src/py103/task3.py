from to_do import TODO


def task3(number: int) -> int:
    multi = 1
    while number>0:
        multi = multi * number
        number -= 1
    return multi


if __name__ == '__main__':
    #Input = 5, output = 120
    print(task3(5))

    #Input = 0, output = 1
    print(task3(0))

