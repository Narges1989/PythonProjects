# TODO("Delete this 'TODO' and create your function here")
def harshad(number: int) -> bool:
    if number == 0:
        return False
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit)

    if number % sum_digit == 0:
        return True
    else:
        return False
