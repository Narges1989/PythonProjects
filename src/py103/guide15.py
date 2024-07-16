from to_do import TODO


def guide15(a: int, b: int) -> int:
    Multi = 1
    if a<b:
        for i in range(a,b+1):
            if i%2==1:
                Multi = Multi*i
        return Multi
    else:
        return -1

if __name__ == '__main__':
    #a=1, b=5 output = 15
    print(guide15(1,5))

    #a=5, b=0, output = -1
    print(guide15(5,0))
