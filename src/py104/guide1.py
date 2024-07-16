from to_do import TODO


def guide1(items: list[int]) -> int:
    if len(items)<6:
        return -1
    return items[0]*items[2]*items[4]*items[-1]


if __name__ == "__main__":
    # items = [1,2,3,4,5,6] , output = 90
    print(guide1([1,2,3,4,5,6]))




