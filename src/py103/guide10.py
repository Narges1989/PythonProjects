from to_do import TODO


def guide10(a: int, b: int, c: int) -> bool:
    return a+b>c and a+c>b and b+c>a

if __name__ == '__main__':
    #a=30,b=30, c=10, output = False
    print(guide10(30,30,10))

    #a=30,b=20, c=10, output = True
    print(guide10(30,20,10))

    #a=30,b=30, c=30, output = True
    print(guide10(30,30,30))

