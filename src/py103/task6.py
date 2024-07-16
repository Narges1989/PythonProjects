from to_do import TODO


def task6(number: int) -> int:
    num = str(number)
    reverse_num = num[::-1]
    result = int(reverse_num)
    return result


if __name__ == '__main__':
    #Input = 543, output = 345
    print(task6(543))

    #Input = 134, output = 431
    print(task6(134))

