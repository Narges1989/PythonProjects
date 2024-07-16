from to_do import TODO


def task4() -> int:
    sum = 0
    for number in range(1,1000):
        if number % 9 == 0:
            sum = sum + number
    return sum