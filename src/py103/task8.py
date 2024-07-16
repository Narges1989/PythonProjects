from to_do import TODO


def task8(number: int) -> int:
    num_str = str(number)
    sum = 0
    for digit in num_str:
        sum = sum + int(digit)
    return sum
