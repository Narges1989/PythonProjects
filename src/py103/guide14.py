from to_do import TODO


def guide14(a: int, b: int) -> int:
    sum = 0
    if a<b:
        for i in range(a,b+1):
            if i%2 == 0:
                sum = sum + i
        return sum
    else:
        return -1


if __name__ == '__main__':
    #a=0, b=5 output = 6
    print(guide14(0,5))

    #a=5, b=0, output = -1
    print(guide14(5,0))
