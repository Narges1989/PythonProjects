from to_do import TODO


def guide4(length: float) -> float:
    result = 4*length
    return result

if __name__== "__main__":
    # length = 5 -> 20
    print(guide4(5))

    # length = 0 -> 0
    print(guide4(0))

    #length = 100 -> 400
    print(guide4(100))