from to_do import TODO


def guide8(day: int) -> str:
    if day == 1:
        return 'monday'
    elif day == 2:
        return 'tuesday'
    elif day == 3:
        return 'wednesday'
    elif day == 4:
        return 'thursday'
    elif day == 5:
        return 'friday'
    elif day == 6:
        return 'saturday'
    elif day == 7:
        return 'sunday'
    else:
        return 'error'


if __name__ == "__main__":
    # day = 3, output = wednesday
    print(guide8(3))

    # month = 6, output = saturday
    print(guide8(7))

    # day = -1 , output = error
    print(guide8(-1))

