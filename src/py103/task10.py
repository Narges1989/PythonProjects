from to_do import TODO


def task10(password: str) -> bool:
    d = l = u = s = 0
    if len(password) in range(6,11):
        for element in password:
            if element.isdigit():
                d += 1
            elif element.islower():
                l += 1
            elif element.isupper():
                u += 1
            elif element == '$' or element == '#' or element == '@' :
                s += 1
    if d>=1 and l>=1 and u>=1 and s >= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    #temperature: bc12#76j, output = True
    print(task10('Bc12#76j'))

    #temperature: bn&sd3, output = False
    print(task10('bn&sd3'))


