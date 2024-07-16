from to_do import TODO


def task5(value_for_a: int, value_for_b: int) -> tuple[int, int]:
    a = value_for_a
    b = value_for_b

    temp = a
    a = b
    b = temp

    # Do not erase or change the below statement
    return a, b

if __name__ == '__main__':
    # a=2, b=1, output: a=1, b=2
    print(task5(2,1))

    # a=5, b=3, output: a=3, b=5
    print(task5(5, 3))