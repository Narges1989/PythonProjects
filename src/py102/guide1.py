from to_do import TODO


def guide1(length: float, width: float, height: float) -> float:
    result = length * width * height

    return result

if __name__ == "__main__":
    print(guide1(5,10, 10))
    print(guide1(0,0, 0))
    print(guide1(1,1, 1))