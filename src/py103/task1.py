from to_do import TODO


def task1(a: int, b: int) -> int:
    sum = 0
    if a>=b:
        return 0
    else:
        for number in range(a,b+1):
            sum = sum + number
        return sum


if __name__ == '__main__':
    #a=1,b=5, output = 15
    print(task1(1,5))
    #a=3,b=3, output = 0
    print(task1(3,3))