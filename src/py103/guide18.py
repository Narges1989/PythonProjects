from to_do import TODO


def guide18(a: int, b: int) -> int:
    multi = 1
    if a<b:
        for number in range(a,b+1):
            if number%5 == 0:
                multi = multi * number
        return multi
    elif a>b:
        return -1
    else:
        return 1