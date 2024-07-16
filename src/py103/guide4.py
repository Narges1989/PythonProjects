from to_do import TODO


def guide4(pin: int) -> bool:
    return (pin == 5678)


if __name__== "__main__":
    # pin = 5678, output = True
    print(guide4(5678))

    # pin=1918 , output = False
    print(guide4(1918))

