from to_do import TODO


def guide7(month: int) -> str:
    if month in range(3,6):
        return 'spring'
    elif month in range(6,9):
        return 'summer'
    elif month in range(9,12):
        return 'fall'
    elif month == 12 or month == 1 or month == 2:
        return 'winter'
    else:
        return 'error'


if __name__ == "__main__":
    # month = 3, output = sprint
    print(guide7(3))

    # month = 7, output = summer
    print(guide7(7))

    # month = 10 , output = fall
    print(guide7(10))

    # month = 1 , output = winter
    print(guide7(1))
