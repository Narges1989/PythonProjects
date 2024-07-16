from to_do import TODO


def guide11(a: int, b: int, c: int) -> str:
    if a==b==c:
        return 'equilateral'
    elif a==b or a==c or b==c:
        return 'isosceles'
    else:
        return 'scalene'

if __name__ == '__main__':
    #a=17,b=15, c=8, output = scalene
    print(guide11(17,15,8))

    #a=30,b=30, c=10, output = isosceles
    print(guide11(30,30,10))

    #a=30,b=30, c=30, output = equilateral
    print(guide11(30,30,30))

