from to_do import TODO


def guide3(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False

if __name__== "__main__":
    # age = 20 , output = True
    print(guide3(20))

    # age = 15 , output = False
    print(guide3(15))

