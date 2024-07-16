# TODO("Delete this 'TODO' and create your function here")
def bonus(numbers: list[int]):
    for index,number in enumerate(numbers):
        numbers[index] = number + 1


if __name__ == '__main__':
    grades = [1,2,3]
    bonus(grades)
    print(grades)