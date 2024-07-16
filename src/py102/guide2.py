from to_do import TODO


def guide2(base: float, height: float) -> float:
    result = (base * height)/2
    return result

if __name__ == "__main__":
    print(guide2(5,10))
    print(guide2(0,0))
    print(guide2(5,2))
