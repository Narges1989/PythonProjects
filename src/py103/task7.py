from to_do import TODO


def task7(a: int, b: int) -> int:
    iteration = 0
    result = 1
    while iteration < b:
        result = result * a
        iteration += 1
    return result


if __name__ == '__main__':
    #a=5,b=2, output = 25
    print(task7(5,2))

    #a=3, b= 4, output = 81
    print(task7(3,4))

