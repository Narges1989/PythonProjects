from to_do import TODO


def guide6(age: int) -> str:
    if age in range(0,2):
        return 'infant'
    elif age in range(2,5):
        return 'toddler'
    elif age in range(5,13):
        return 'child'
    elif age in range(13,20):
        return 'teen'
    elif age in range(20,40):
        return 'adult'
    elif age in range(40,60):
        return 'middle adult'
    else:
        return 'senior adult'


if __name__ == "__main__":
    # age = 10, output = child
    print(guide6(10))

    # age = 40, output = middle adult
    print(guide6(40))

    # age = 0 , output = infant
    print(guide6(0))

    # age = 60 , output = senior adult
    print(guide6(60))

    # age = 30 , output = adult
    print(guide6(30))

    # age = 2 , output = toddler
    print(guide6(2))

    # age = 14 , output = teen
    print(guide6(14))
